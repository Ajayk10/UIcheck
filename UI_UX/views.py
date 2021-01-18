from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import *
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import *
from  .forms import *

# Create your views here.

def  LikeView(request,pk):
    post = get_object_or_404(Post,id = request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article',args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-post_date']


class ArticleDetail(DetailView):
    model = Post
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Post,id = self.kwargs['pk'])
        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True
        total_likes = stuff.total_likes() + 10
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


    



class AddFeedView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addfeed.html'
    # fields = '__all__'

class UpdateFeedView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'updatefeed.html'

class DeleteFeedView(DeleteView):
    model = Post
    template_name = 'deletefeed.html'
    success_url = reverse_lazy('index')