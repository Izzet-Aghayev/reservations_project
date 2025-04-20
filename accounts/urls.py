from django.urls import path

from accounts import views as accounts_views



urlpatterns = [
    path('register/', accounts_views.RegisterView.as_view(), name='register'),
    path('login/', accounts_views.LoginView.as_view(), name='login'),
]
