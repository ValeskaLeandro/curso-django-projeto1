from django.urls import path

from recipes import views  # posso usar . no lugar de recipes

urlpatterns = [
    path('', views.home),  # Home
    path('recipes/<int:id>/', views.recipe),
]
