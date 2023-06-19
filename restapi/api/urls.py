"""
URL configuration for restapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from api import views

urlpatterns = [
    path('users/', views.get_all_users),
    path('users/<str:pk>/', views.get_user_by_pk),
    path('users/create/', views.create_user),
    path('users/delete/', views.delete_all_users),
    path('users/delete/<str:pk>/', views.delete_user_by_pk),
    path('users/update/<str:pk>/', views.update_user),
    path('transactions/', views.get_all_transactions),
    path('transactions/<int:transaction_id>/', views.get_transaction_by_id),
    path('transactions/create/', views.create_transaction),
]
