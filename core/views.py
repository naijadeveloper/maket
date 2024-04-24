from django.shortcuts import render

# Create your views here.
def index(request):
  """request: info abt browser, ip addy, if get/post/put request e.tc"""
  return render(request, "core/index.html")