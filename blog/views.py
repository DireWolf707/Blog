from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('title','body',)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ('title','body',)

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'post'