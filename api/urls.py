from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.getProducts),
    path('products/<str:pk>/', views.getProduct)
]
