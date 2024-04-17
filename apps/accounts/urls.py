from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter
from djoser.views import UserViewSet

from django.urls import path

app_name = 'accounts'
router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token-verify'),
]

urlpatterns += router.urls
