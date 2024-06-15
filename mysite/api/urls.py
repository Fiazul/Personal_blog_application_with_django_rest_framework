from django.urls import path
from . import views
from .views import blogPostListCreate

urlpatterns = [
    path("blogpost/",views.blogPostListCreate.as_view(),name="blogpost_view_create"),
    path("blogpost/<int:pk>/",views.blogPostRetriveUpdateDestroy.as_view(),name="Update")
]
