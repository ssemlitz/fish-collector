from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('fishies/', views.fishies_index, name='fishies_index'),
  path('fishies/<int:fish_id>/', views.fishies_detail, name='fishies_detail'),
  path('fishies/create/', views.FishCreate.as_view(), name='fishies_create'),
  path('fishies/<int:pk>/update/', views.FishUpdate.as_view(), name='fishies_update'),
  path('fishies/<int:pk>/delete/', views.FishDelete.as_view(), name='fishies_delete'),
]