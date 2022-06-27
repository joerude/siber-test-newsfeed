from django.contrib.auth.views import LogoutView
from django.urls import path

from config.settings import base
from .views import SignUpUser, SignInUser, AddNews, HomeListView, NewsDetailView

urlpatterns = [
    path('', HomeListView.as_view(), name='index'),
    path('news/<slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('signup/', SignUpUser.as_view(), name='signup'),
    path('signin/', SignInUser.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': base.LOGOUT_REDIRECT_URL}, name='signout', ),
    path('add_news/', AddNews.as_view(), name='add_news'),
]
