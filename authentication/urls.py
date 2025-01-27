from django.urls import path
from rest_framework_simplejwt import views as auth_views
from . import views


urlpatterns = [
    path('token/', auth_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', auth_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', auth_views.TokenVerifyView.as_view(), name='token_verify'),
    path('create-user/', views.UserCreateAPIView.as_view(), name="create_user")
]
