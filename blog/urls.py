from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail' ),
    path('post/new/', PostCreateView.as_view(), name='post-create' ),
    path('about/',views.about,name='blog-about'),
    #path('create/', views.create, name="create"),

]
urlpatterns += staticfiles_urlpatterns()