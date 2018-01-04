from django.urls import path, include

from . import views

urlpatterns = [

    path('test-url/', views.test, name='test'),
    path('google-stats/', views.google, name='google'),
    path('string-stats/', views.string_stats, name='string_stats'),
    
]