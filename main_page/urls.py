
from django.urls import path
from . import views

urlpatterns = [

    path('', views.BookApiView.as_view(), name='main'),
    path('comment', views.CommentApiView.as_view(), name='comment')
]