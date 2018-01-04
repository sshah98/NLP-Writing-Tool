from django.urls import path, include

from . import views

urlpatterns = [

    path('test-url/', views.test, name='test'),
    
    path('google-url/', views.google, name='google'),
]