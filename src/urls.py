from django.urls import path, include

from src import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', views.main),
    path('profile/', views.some_view),
    path('sentry/', views.my_view),
]
