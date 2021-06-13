from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListDaily.as_view()), #日報一覧
    path('<int:pk>/', views.DetailDaily.as_view()), #一日の詳細
    path('<int:cat>/', views.CategoryDaily.as_view()), #カテゴリ別一覧
]

