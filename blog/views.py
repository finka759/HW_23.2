from pytils.translit import slugify
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Edit


class EditCreateView(CreateView):
    model = Edit
    fields = ('title', 'content', 'image', 'created_at', 'is_published', 'slug', 'count_of_views',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_edit = form.save()
            new_edit.slug = slugify(new_edit.title)
        return super().form_valid(form)


class EditUpdateView(UpdateView):
    model = Edit
    fields = ('title', 'content', 'image', 'created_at', 'is_published', 'slug', 'count_of_views',)

    def form_valid(self, form):
        if form.is_valid():
            new_edit = form.save()
            new_edit.slug = slugify(new_edit.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:view', args={self.kwargs.get('pk')})


class EditListView(ListView):
    model = Edit

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class EditDetailView(DetailView):
    model = Edit

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_of_views += 1
        self.object.save()
        return self.object


class EditDeleteView(DeleteView):
    model = Edit
    success_url = reverse_lazy('blog:list')
