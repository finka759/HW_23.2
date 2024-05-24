from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Edit


class EditCreateView(CreateView):
    model = Edit
    fields = ('title', 'content', 'image', 'created_at', 'is_published', 'slug', 'count_of_views',)
    success_url = reverse_lazy('blog:list')


class EditUpdateView(UpdateView):
    model = Edit
    fields = ('title', 'content', 'image', 'created_at', 'is_published', 'slug', 'count_of_views',)
    success_url = reverse_lazy('blog:list')


class EditListView(ListView):
    model = Edit


class EditDetailView(DetailView):
    model = Edit

class EditDeleteView(DeleteView):
    model = Edit
    success_url = reverse_lazy('blog:list')
