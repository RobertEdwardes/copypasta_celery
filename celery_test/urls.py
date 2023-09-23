# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.widget_list, name='widget_list'),
    path('create_widget/', views.create_widget, name='create_widget'),
    path('update_widget/<int:widget_id>/', views.update_widget, name='update_widget'),  # Add this line
]