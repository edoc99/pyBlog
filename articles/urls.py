from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list),
    # named capturing group
    path('<slug:slug>/', views.article_detail),
]
