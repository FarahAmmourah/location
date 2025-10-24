from django.contrib import admin
from django.urls import path, include
from maps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('select-location/', views.map_page),
]
