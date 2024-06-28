from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import models


class ArticleListView(LoginRequiredMixin, ListView):
    model = models.Article
    template_name = 'article_list.html'
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = models.Article
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Article
    fields = ['title', 'body']
    template_name = 'article_edit.html'
    login_url = 'login'

    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = 'article_new.html'
    fields = ['title', 'body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
