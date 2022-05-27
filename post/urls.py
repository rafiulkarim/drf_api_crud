from django.urls import URLPattern, path

from . import views

urlpatterns = [
    # post CRUD
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),

    #Comment CRUD
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommenttDetail.as_view()),
]