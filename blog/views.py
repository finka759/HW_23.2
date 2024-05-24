from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from blog.models import Edit


class EditCreateView(CreateView):
    model = Edit
    fields = ('title', 'content', 'image', 'created_at', 'is_published', 'slug', 'count_of_views',)
    success_url = reverse_lazy('blog:list')


class EditListView(ListView):
    model = Edit
