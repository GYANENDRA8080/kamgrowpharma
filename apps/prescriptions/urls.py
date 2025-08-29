from django.urls import path
from . import views
app_name = 'prescriptions'
urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('thanks/', views.thanks, name='thanks'),
]
