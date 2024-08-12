from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Item, User
from .forms import NewItemForm, EditItemForm, ItemRatingForm
from dashboard.models import Cart
#####
import random

# Create your views here.
def browse(request):
  query = request.GET.get("query", '')
  items = []
  user = []

  if query:
    print("in query")
    items = Item.objects.filter(is_sold=False)
    items = items.filter(Q(name__icontains=query))# | Q(description__icontains=query)
    user = User.objects.filter(Q(username__iexact=query))
    
  
  if user:
    print("in user")
    # get all items from user
    all_items_from_user = user[0].items.filter(is_sold=False)
    
    # extend items list with the list above
    items = list(items)
    items.extend(all_items_from_user)


  if not request.user.is_authenticated:
    items = items[0:3]

  print(items)

  #..............................
  return render(request, "item/browse.html", {
    "items": items,
    "query": query
  })


def detail(request, pk, cart=None):
  item = get_object_or_404(Item, pk=pk)
  related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)
  related_items_count = related_items.count()
  random_related_items = random.sample(list(related_items), 4 if related_items_count > 4 else related_items_count)

  # get item's ratings
  item_ratings = item.item_ratings.all()
  high_nd_low_ratings = sorted(item_ratings, key=lambda rating: rating.rate, reverse=True)

  if high_nd_low_ratings:
    if len(high_nd_low_ratings) >= 2:
      item_ratings = [high_nd_low_ratings[0], high_nd_low_ratings[len(high_nd_low_ratings) - 1]]
    else:
      item_ratings = [high_nd_low_ratings[0]]
  else:
    item_ratings = []
  
  item_ratings_count = item.item_ratings.count()

  # is there a cart for this item and user
  user_item_cart =  None
  
  if request.user.is_authenticated:
    user_item_cart = request.user.carts.filter(item=item)

  if user_item_cart:
    user_item_cart = user_item_cart[0]

  # if cart is 'add' create cart for item
  if request.user.is_authenticated and not user_item_cart and cart == "add_to_cart":
    cart = Cart(created_by=request.user, item=item)
    cart.save()
    return redirect("item:detail", pk=pk)
  
  # if cart is 'delete' remove cart
  if request.user.is_authenticated and user_item_cart and cart == "remove_from_cart":
    cart = Cart.objects.filter(created_by=request.user, item=item)
    if cart:
      cart = cart[0]
      cart.delete()
    return redirect("item:detail", pk=pk)


  return render(request, "item/detail.html", {
    "item": item,
    "user_item_cart": user_item_cart,
    "related_items": random_related_items,
    "item_ratings": item_ratings,
    "item_ratings_count": item_ratings_count
  })


@login_required
def reviews(request, pk):
  item = get_object_or_404(Item, pk=pk)
  
  # get all reviews and separate user's from all of them
  item_ratings = item.item_ratings.all().exclude(created_by=request.user)
  my_item_rating = item.item_ratings.filter(created_by=request.user)
  
  # get user's
  if my_item_rating:
    my_item_rating = my_item_rating[0]
  else:
    my_item_rating = None

  # handle request.POST
  if request.method == "POST":
    form = ItemRatingForm(request.POST, request.FILES, instance=my_item_rating)

    if form.is_valid():
      item_rating = form.save(commit=False)
      item_rating.created_by = request.user
      item_rating.rated_item = item
      item_rating.save()

      return redirect("item:reviews", pk=item.id)
  else:
    form = ItemRatingForm(instance=my_item_rating)
  

  return render(request, "item/reviews.html", {
    "item": item,
    "item_ratings": item_ratings,
    "my_item_rating": my_item_rating,
    "form": form
  })


@login_required
def newItem(request):
  if request.method == "POST":
    form = NewItemForm(request.POST, request.FILES)

    if form.is_valid():
      item = form.save(commit=False)
      item.created_by = request.user
      item.save()

      return redirect("item:detail", pk=item.id)
  else:
    form = NewItemForm()

  return render(request, "item/form.html", {
    "form": form,
    "title": "Add a new item on sale"
  })


@login_required
def editItem(request, pk):
  item = get_object_or_404(Item, pk=pk, created_by=request.user)

  if request.method == "POST":
    form = EditItemForm(request.POST, request.FILES, instance=item)

    if form.is_valid():
      form.save()

      return redirect("item:detail", pk=item.id)
  else:
    form = EditItemForm(instance=item)

  return render(request, "item/form.html", {
    "form": form,
    "title": "Edit Item"
  })


@login_required
def delete(request, pk):
  item = get_object_or_404(Item, pk=pk, created_by=request.user)
  item.delete()

  return redirect("dashboard:index")