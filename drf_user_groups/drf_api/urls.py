from django.urls import path
from rest_framework.authtoken import views as drfviews
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('users/', views.UserView.as_view()),
    path('api-token-auth/', drfviews.obtain_auth_token),
    path('JSON-token/', obtain_jwt_token)
]