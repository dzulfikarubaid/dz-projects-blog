from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import WriteForm

# Create your views here.
class WindowView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-post_date','-id']

class PostView(DetailView):
    model = Post
    template_name = 'post.html'

class WriteView(CreateView):
    model = Post
    template_name = 'write.html'
    form_class = WriteForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update.html'
    form_class = WriteForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('window')