from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blogentry.models import Blogentry


class BlogentryCreateView(CreateView):
    model = Blogentry
    fields = ('title', 'content')
    success_url = reverse_lazy('blogentry:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)



class BlogentryListView(ListView):
    model = Blogentry

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=False)

        return queryset

class BlogentryDetailView(DetailView):
    model = Blogentry

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class BlogentryUpdateView(UpdateView):
    model = Blogentry
    fields = ('title', 'content')
    #success_url = reverse_lazy('blogentry:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogentry:view', args=[self.kwargs['pk']])



class BlogentryDeLeteView(DeleteView):
    model = Blogentry
    success_url = reverse_lazy('blogentry:list')

