from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from item.models import Item, Category, User
from .forms import UserRatingForm, ProfileUpdateForm

# Create your views here.
@login_required
def index(request):
  return render(request, "dashboard/index.html")


def profile(request, username=None):
  # if url = 'dashboard/enoch_items/' and enoch_items is logged in
  # then just go to 'dashboard/profile'
  if username == request.user.username:
    return redirect("dashboard:profile")
  
  if not username:
    username = request.user.username

  # get the user and get the user's profile, every user has a profile
  user = get_object_or_404(User, username=username)
  profile = user.profile.all()

  if profile:
    profile = profile[0]

  # say I am logged in and I want to check the profile
  # of another user, I would like to know if I rated the user and separate
  # my rating from the rest of the ratings
  # so "request_user_rating" is the rating I gave this user
  request_user_rating = None # initially None

  if request.user.is_authenticated: # but is I am logged in get my rating, if exist
    request_user_rating = request.user.user_ratings.filter(rated_user=user) or None

  if request_user_rating:
    request_user_rating = request_user_rating[0]
  
  # get all the ratings that this user received, minus mine, cause
  # if I rated this user, I already got that above
  # except when no one is logged in, then just get only 2 out of it
  if request.user.is_authenticated:
    user_ratings = user.user_rated.exclude(created_by=request.user)
  else:
    user_ratings = user.user_rated.all()
    user_ratings = user_ratings[0:2]
  
  # set profile banner static link
  profile_banner = f"banners/banner {profile.banner_number if profile else 1}.jpg"

  # form is initially none
  form = None

  if request.user.is_authenticated:
    # handle request.POST
    if request.method == "POST":
      form = UserRatingForm(request.POST, request.FILES, instance=request_user_rating)

      if form.is_valid():
        user_rating = form.save(commit=False)
        user_rating.created_by = request.user
        user_rating.rated_user = user
        user_rating.save()

        return redirect("dashboard:other_user_profile", username=user.username)
    else:
      form = UserRatingForm(instance=request_user_rating)

  return render(request, "dashboard/profile.html", {
    "user": user,
    "form": form,
    "request_user_rating": request_user_rating,
    "user_ratings": user_ratings,
    "profile": profile,
    "profile_banner": profile_banner
  })


@login_required
def cart(request, cart_id=None):
  all_carts = request.user.carts.all()

  if cart_id:
    cart = request.user.carts.filter(pk=cart_id)

    if cart:
      cart = cart[0]
      cart.delete()

    return redirect("dashboard:cart")

  return render(request, "dashboard/cart.html", {
    "all_carts": all_carts
  })


@login_required
def categories(request):
  query = request.GET.get("query", '')
  items = []
  categories_nd_item_number = {}

  categories = Category.objects.all()
  categories = sorted(categories, key=lambda category: len(category.items.filter(created_by=request.user)), reverse=True)

  # get all categories and items in each that were created by request.user
  for category in categories:
    category_name = category.name
    all_items = category.items.filter(created_by=request.user)

    # add to categories
    categories_nd_item_number[category_name] = [len(all_items), category.description]


  # if query, get the category and then get items
  # else if empty, set it to the name of first category and then get items
  if query:
    # find the category whose name is the query
    # category = categories.filter(name__iexact=query)[0]
    category = list(filter(lambda category: query == category.name, categories))[0]

    # get all items from category created_by request.user
    if category:
      items = category.items.filter(created_by=request.user)
  else:
    query = categories[0].name

    # find the category whose name is the query
    # category = categories.filter(name__iexact=query)[0]
    category = list(filter(lambda category: query == category.name, categories))[0]

    # get all items from category created_by request.user
    if category:
      items = category.items.filter(created_by=request.user)


  # items = Item.objects.filter(created_by=request.user)
  # categories = list(set((map(lambda item: item.category, items))))

  return render(request, "dashboard/categories.html", {
    "items": items,
    "categories": categories_nd_item_number,
    "query": query
  })


@login_required
def settings(request):
  user = request.user

  profile_instance = user.profile.all() or None

  if profile_instance:
    profile_instance = profile_instance[0]

  # handle request.POST
  if request.method == "POST":
    form = ProfileUpdateForm(request.POST, request.FILES, instance=profile_instance)

    if form.is_valid():
      user_profile = form.save(commit=False)
      user_profile.created_by = user
      user_profile.save()

      return redirect("dashboard:profile")
  else:
    form = ProfileUpdateForm(instance=profile_instance)

  
  return render(request, "dashboard/settings.html", {
    "form": form
  })


@login_required
def logout_user(request):
  logout(request)
  return redirect("core:index")