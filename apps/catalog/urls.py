from django.urls import path
from . import views
app_name = 'catalog'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:slug>/', views.product_list, name='category'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
