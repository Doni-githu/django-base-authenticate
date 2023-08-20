from . import views
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/register/', views.Register.as_view(), name="register")
]
