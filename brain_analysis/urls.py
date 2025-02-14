"""
URL configuration for brain_analysis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Panel administracyjny Django
    path('admin/', admin.site.urls),

    # API Endpoints
    path('api/', include('api.urls')),

    # Tokeny JWT dla autoryzacji
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Strona główna i frontend
    path('', include('frontend.urls')),  

    # Logowanie i wylogowanie użytkownika
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Rejestracja użytkownika (jeśli masz widok w Django)
    path('register/', include('frontend.urls')),  # Strona rejestracji

    path('accounts/', include('django.contrib.auth.urls')),  # Obsługa logowania i wylogowywania
]


