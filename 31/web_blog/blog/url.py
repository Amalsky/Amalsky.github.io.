from django.urls import  path
from. import views
from .views import  PostListView,PostDetailView,PostCreateView

urlpatterns = [
    #path("",views.home,name='blog-home'),
    path("",PostListView.as_view(),name='blog-home'),
    path("new/",PostCreateView.as_view(),name='post-new'),
    path("post/<int:pk>/",PostDetailView.as_view(),name='post-detail'),
]