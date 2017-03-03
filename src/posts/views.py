from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from .forms import PostForm
from .models import Post

# Create your views here.
from .models import Post
def posts_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print (form.cleaned_data.get('title'))
        instance.save()
        messages.success(request,"Success! Well done!")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Nope! Not done!")
    # if request.method == 'POST':
    #     print (request.POST.get("content"))
    #     print (request.POST.get("title"))
    context={
        "form": form,
    }
    return render(request,"post_form.html",context)
    
def posts_detail(request,id=None):
    #instance = Post.objects.get(id=1) 
    print ('Details Page being called')
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

def posts_update(request,id=None):
   
    instance = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None,instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print (form.cleaned_data.get('title'))
        instance.save()
        messages.success(request,"<a href='#'>Success!</a> Well done!",extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context_data={
        "title": instance.title,
        "instance":instance,
        "form":form

    }
    return render(request,"post_form.html",context_data)

def posts_delete(request,id=None):
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,"<a href='#'>Success!</a> Well done deleted!",extra_tags='html_safe')
    return redirect('list')
    

