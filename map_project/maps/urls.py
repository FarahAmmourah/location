from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_page, name='map-page'),
    path('save/', views.save_location, name='save-location'),
]
