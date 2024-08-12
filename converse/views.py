from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from .forms import ConverseMessageForm
from .models import Converse

# Create your views here.
@login_required
def new_converse(request, item_pk):
  item = get_object_or_404(Item, pk=item_pk)

  # if you are owner of item, you shouldn't
  # be able to create a converse with yourself
  if request.user == item.created_by:
    return redirect("item:detail", pk=item_pk)
  
  # get the converse whose item is same as the item above and
  # that the request.user belongs to 
  converse = Converse.objects.filter(item=item).filter(members__in=[request.user.id])

  # if converse already exist
  # redirect to that converse
  if converse:
    return redirect("converse:detail", pk=converse.first().id)

  if request.method == "POST":
    form = ConverseMessageForm(request.POST)

    if form.is_valid():
      converse = Converse.objects.create(item=item)
      converse.members.add(request.user)
      converse.members.add(item.created_by)
      converse.save()

      # create converse message
      converse_msg = form.save(commit=False)
      converse_msg.converse = converse
      converse_msg.created_by = request.user
      converse_msg.save()

      return redirect("item:detail", pk=item_pk)
    
  else:
    form = ConverseMessageForm()

  return render(request, "converse/new.html", {
    "seller": item.created_by,
    "form": form
  })


@login_required
def inbox(request):
  converses = Converse.objects.filter(members__in=[request.user.id])

  return render(request, "converse/inbox.html", {
    "converses": converses,
  })


@login_required
def detail(request, pk):
  converse = Converse.objects.filter(members__in=[request.user.id]).get(pk=pk)

  if request.method == "POST":
    form = ConverseMessageForm(request.POST)

    if form.is_valid():
      converse_message = form.save(commit=False)
      converse_message.converse = converse
      converse_message.created_by = request.user
      converse_message.save()

      converse.save()

      return redirect("converse:detail", pk=pk)
  else:
    form = ConverseMessageForm()

  return render(request, "converse/detail.html", {
    "converse": converse,
    "form": form
  })