from django.urls import path
from .views import RegisterView, LoginView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Custom JWT view
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
