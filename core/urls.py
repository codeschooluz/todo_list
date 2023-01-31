
from django.contrib import admin
from django.urls import path,include
from todoAPI import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.CreateTodoView.as_view(), name='add'),
    path('get/', views.GetAllTodoView.as_view(), name='get'),
    path('remove/<int:id>/', views.RemoveTodoView.as_view(), name='remove'),

    path('auth/', include('rest_framework.urls')),

]
