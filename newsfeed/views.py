from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import View
from django.views.generic import CreateView, ListView, DetailView

from .forms import SignUpForm, SignInForm
from .models import News


class HomeListView(ListView):
    template_name = 'newsfeed/home.html'
    model = News
    paginate_by = 10

    ordering = ['-created_at']

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    
class NewsDetailView(DetailView):
    model = News
    template_name = 'newsfeed/news_detail.html'


class AddNews(CreateView):
    template_name = 'newsfeed/add_news.html'
    model = News
    fields = ('title', 'content',)
    # fields = ('title', 'content', 'image',)
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        news = form.save(commit=False)
        news.slug = slugify(news.title)
        return super(AddNews, self).form_valid(form)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)


class SignUpUser(CreateView):
    form_class = SignUpForm
    template_name = "newsfeed/signup.html"
    success_url = reverse_lazy("signin")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("index")


class SignInUser(LoginView):
    form_class = SignInForm
    template_name = "newsfeed/signin.html"

    def get_success_url(self):
        return reverse_lazy("index")


def logout_user(request):
    logout(request)
    return redirect("signin")


# Create your views here.
def get_view(request):
    print(request.GET)
    print(request.GET.get('paginate_by'))
    return render(request, "newsfeed/get_form.html")


def post_view(request):
    print(request.POST)
    print(request.POST.get('paginate_by'))
    return render(request, "newsfeed/post_form.html")
