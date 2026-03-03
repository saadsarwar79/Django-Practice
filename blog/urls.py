# from django.urls import path
# from blog import views
# app_name = 'blog'

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('post/<int:id>/', views.post_detail, name='post_detail'),
#     path('create/', views.post_create, name='post_create'),
#     path('post/<int:id>/edit/', views.post_update, name='post_update'),
#     path("register/", views.register, name="register"),
#     path("", views.PostListView.as_view(), name="post_list"),
# ]
from django.urls import path
from blog import views

app_name = 'blog'
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'api/posts', PostViewSet)

# urlpatterns += router.urls
urlpatterns  = router.urls + [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('post/<int:id>/edit/', views.post_update, name='post_update'),
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),
    path("register/", views.register, name="register"),
]