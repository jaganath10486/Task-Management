from django.urls import path
from rest_framework_simplejwt import views as jwtviews;
from .views import UserRegister

urlpatterns = [
    path('token', jwtviews.TokenObtainPairView.as_view(), name='Token Obtain'),
    path('token/refresh', jwtviews.TokenRefreshView.as_view(), name='Toeken Refresh view' ),
    path('register/', UserRegister.as_view(), name="Register")
]

