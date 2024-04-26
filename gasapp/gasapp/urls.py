from django.urls import path
from django.contrib.auth import views as auth_views 
from consumer_services import views

urlpatterns = [
    

    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('submit_request/', views.submit_request, name='submit_request'),
    path('success/', views.success, name='success'),
    path('view_requests/', views.view_requests, name='view_requests'),
]

