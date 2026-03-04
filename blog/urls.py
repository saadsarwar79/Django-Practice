from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),  # HTML homepage
    path("post/<int:id>/", views.post_detail, name="post_detail"),
    path("create/", views.post_create, name="post_create"),
    path("post/<int:id>/edit/", views.post_update, name="post_update"),
    path("post/<int:id>/delete/", views.post_delete, name="post_delete"),
    path("register/", views.register, name="register"),
]