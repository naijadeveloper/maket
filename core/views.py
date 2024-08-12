from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from item.models import Category, Item
from .forms import SignupForm
########
import random
import math

# Create your views here.
def index(request):
  categories = Category.objects.all()
  categories = sorted(categories, key=lambda category: category.items.count(), reverse=True)
  structured_categories_dict = {}

  for category in categories:
    category_id = category.id
    items_count = category.items.count()
    random_items = []

    if items_count > 0:
      random_items = random.sample(list(category.items.all()), 3 if items_count > 3 else items_count)

    # {"toys and games": [10, [rand_item 1, rand_item 2, ... ]]}
    structured_categories_dict[category] = [items_count, random_items, category_id]

  return render(request, "core/index.html", {
    "categories": structured_categories_dict,
  })


@login_required
def category(request, pk):
  # implementing pagination
  page = request.GET.get("page", "1")

  category = get_object_or_404(Category, pk=pk)
  category_items = category.items.all()

  no_of_items_per_page = 4
  no_of_pages = math.ceil(category.items.count() / no_of_items_per_page)

  items = []

  # get items for each page
  try:
    page = int(page)

    # if page number is greater than the 'no_of_pages'
    if page > no_of_pages:
      items = "error2"
    else:
      # get (exclusive) last_index and get first_index
      last_index = page * no_of_items_per_page
      first_index = last_index - no_of_items_per_page

      # get items
      items = category_items[first_index:last_index]

  except Exception as err:
    items = "error1"
    

  return render(request, "core/category.html", {
    "page": page,
    "category": category,
    "items": items,
    "no_of_pages": list(range(1, no_of_pages+1))
  })


def contact(request):
  return render(request, "core/contact.html")


def signup(request):
  if request.method == "POST":
    form = SignupForm(request.POST)

    if form.is_valid():
      form.save()

      logout(request)
      return redirect("core:login")
  else:
    form = SignupForm()

  return render(request, "core/signup.html", {
    "form": form
  })