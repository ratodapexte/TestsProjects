from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.
class BlogListView(ListView):
    model = Post #seus modelos de dados serão do tipo POST
    template_name = 'home.html' #seu template será do arquivo home.html

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView): 
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')      
# Usamos reverse_lazy como um oposto para apenas reverse então nã vai executar o redirecionamento da URL até que nossa view tenha \
# realizado o deletamento do post do blog
