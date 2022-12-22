
from django.contrib import admin
from django.urls import path
from todoAPI import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.CreateTodoView.as_view(), name='add')
]
