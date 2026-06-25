from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
path('cameras/', views.cameras, name='cameras'),
path('detection/', views.detection, name='detection'),
path('alerts/', views.alerts, name='alerts'),
path('analytics/', views.analytics, name='analytics'),
path('users/', views.users, name='users'),
path('security/', views.security, name='security'),
path('settings/', views.settings, name='settings'),
path('search/', views.search, name='search'),
path('profile/', views.profile, name='profile'),
path('notifications/', views.notifications, name='notifications'),
path('logout/', views.logout_view, name='logout'),
path('load-data/', views.load_kaggle_data),
]
