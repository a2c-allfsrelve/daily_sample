from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListDaily.as_view()), #日報一覧
    path('<int:pk>/', views.DailyDetail.as_view()), #一日の詳細
    path('<int:cat>/', views.Category.as_view()), #カテゴリ別一覧
]

