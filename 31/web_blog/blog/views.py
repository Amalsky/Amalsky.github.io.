from django.shortcuts import render
from .models import post
from django.views.generic import  ListView,DetailView,CreateView

def home(request):
    context={'posts':post.objects.all()}
    return render(request,"blog/home.html",context)

class PostListView(ListView):
     model = post
     template_name = 'blog/home.html'
     context_object_name = 'posts'
     ordering = ['-date']

class PostDetailView(DetailView):
      model = post

class PostCreateView(CreateView):
      model = post
      fields = ['title','content']

      def form_valid(self, form):
          form.instance.author = self.request.user
          return super().form_valid(form)




