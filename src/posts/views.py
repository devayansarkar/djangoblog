from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post
def posts_create(request):
    return HttpResponse("<h1> Create </h1>")
    
def posts_detail(request):
    context_data={
        "title": "Detail"
    }
    return render(request,"index.html",context_data)

def posts_list(request):
    # if request.user.is_authenticated():
    #     context_data={
    #          "title": "My User List"
    #      }
    # else:
    #     context_data={
    #     "title": "unauthernticated User List"
    #      }

    queryset = Post.objects.all()
    context_data={
        "object_list": queryset,
         "title": "List is working"
          }
    return render(request,"index.html",context_data)

def posts_update(request):
    return HttpResponse("<h1> Update </h1>")

def posts_delete(request):
    return HttpResponse("<h1> Delete </h1>")

