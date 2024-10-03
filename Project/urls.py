from django.urls import path
from . import views

urlpatterns = [
  path('', views.page_view, name='page_view'),
  path('Login/', views.login_view, name='login_view'),
  path('logout/', views.logout_view, name='logout_view'),
  path('signup/', views.signup_view, name='signup_view'),
  path('userinfo/', views.userinfo_view, name='userinfo_view'),
  ]