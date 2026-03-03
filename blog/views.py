from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import ListView, DetailView
from django.views.generic import ListView, DetailView
from rest_framework import viewsets, permissions
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
def post_list(request):
    posts = Post.objects.select_related("category").all()
    return render(request, "post_list.html", {"posts": posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "post_detail.html", {"post": post})


# @login_required
# def post_create(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect("blog:post_list")

#     return render(request, "post_form.html", {"form": form})


# @login_required
# def post_update(request, id):
#     post = get_object_or_404(Post, id=id)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect("blog:post_detail", id=post.id)
#     else:
#         form = PostForm(instance=post)

#     return render(request, "post_form.html", {"form": form, "post": post})




def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog:post_list")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect("blog:post_list")
    else:
        form = PostForm()

    return render(request, "post_form.html", {"form": form})


@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect("blog:post_detail", id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, "post_form.html", {"form": form})


@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    post.delete()
    messages.success(request, "Post deleted successfully!")
    return redirect("blog:post_list")