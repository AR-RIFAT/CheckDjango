from django.urls import path
from . import views

urlpatterns = [
    # /music/
    path('', views.index, name='index'),
    # /music/album_id/
    path('<str:album_id>/', views.details, name='details'),
]
