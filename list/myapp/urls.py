from django.http import HttpResponse
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns=[
    path('admin/',admin.site.urls),
    path('', views.index, name='list'),
    path('update_task/<str:pk>/',views.updateTask,name='update'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
]
