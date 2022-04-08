from django.contrib import admin
from django.urls import path
from projetozomato import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('restaurante/<int:id>', views.detalhes_restaurante, name='restaurante')
]
