from django.urls import path
from . import views

urlpatterns = [
    path('', views.mewp, name='mewp'),
    path('add_checksheet/', views.add_checksheet, name='add_checksheet'),
    path('view/<int:id>/', views.view_checksheet, name='view_checksheet'),
    path('delete/<int:id>/', views.delete_checksheet, name='delete_checksheet'),
]