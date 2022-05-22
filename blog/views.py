from django.shortcuts import render
from .models import Blog
# Create your views here.
def allblogs(request):
    blog = Blog.objects
    return render(request, 'blog/allblogs.html', {'blog': blog})