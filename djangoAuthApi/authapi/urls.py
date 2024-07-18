from django.urls import path, include
from authapi.views import UserRegistrationView,UserLoginView,UserProfileView,UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changePassword/', UserChangePasswordView.as_view(), name='changePassword'),
    path('sendResetPasswordEmail/', SendPasswordResetEmailView.as_view(), name='sendResetPasswordEmail'),
    path('resetPassword/<uid>/<token>/', UserPasswordResetView.as_view(), name='resetPassword'),


]