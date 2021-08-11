from django.urls import path
from rest_framework.authtoken import views as drfviews
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('users/', views.UserView.as_view()),
    path('api-token-auth/', drfviews.obtain_auth_token)
]