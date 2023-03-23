from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from .models import post
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.db import models
from .forms import UserModelForm
from django.contrib.auth.decorators import login_required


# Create your views here.
'''posts=[
    {
        'author':'coreyMS',
        'title':'blog post 1',
        'content':"first post content",
        'date_posted':'august 28,2021'
    },
    {
        'author':'chris',
        'title':'blog_post 2',
        'content':'second post content',
        'date_posted':'july 12,1995'
    }
]
'''
# we don't need this data dummy now

def home(request):
    #queuing data from database
    context={
            'posts':post.objects.all()
    }
    return render(request,'blog/home.html',context)


class PostListView(ListView):
    model = post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = post

class PostCreateView(CreateView):
    model = post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)   

def about(request):
    return render(request,'blog/about.html',{'title':'about'})

@login_required
def create(request):         

    if request.method == 'POST':   
        form = UserModelForm(request.POST)    
        if form.is_valid():
            form.save()

            users = post.objects.all()
            #request.user.post.add(u) 

            return redirect('blog-home')

    else:
        form_class = UserModelForm

        return render(request, 'blog/create.html', {
            'form': form_class,
            })
    
    
     
