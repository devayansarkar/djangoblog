from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.
from .models import Post
def posts_create(request):
    return HttpResponse("<h1> Create </h1>")
    
def posts_detail(request,id=None):
    #instance = Post.objects.get(id=1) 
    instance = get_object_or_404(Post,id=id)
    context_data={
        "title": "Detail",
        "instance":instance
    }
    return render(request,"post_detail.html",context_data)

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

