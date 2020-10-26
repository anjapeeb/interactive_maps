from django.urls import path

urlpatterns = [
    path('home/', views.LoginView.as_view(), name='login'),
]