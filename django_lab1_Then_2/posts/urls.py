from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='posts_index'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
            path('author/<int:author_id>/', views.author_detail, name='author_detail'),

]