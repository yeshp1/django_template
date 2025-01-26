from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Post details
]