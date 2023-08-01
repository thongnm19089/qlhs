from django.urls import path
from .api import StudentApi
from . import views
from django.contrib.auth import views as auth_views
app_name = "student"
urlpatterns = [
  path('api',StudentApi.as_view()),
  path('add', views.create_view, name = "views"),
  path('list/', views.view, name="view"),
  path('<int:id>/', views.detail, name="detail"),
  path('<id>/update', views.update, name="update" ),
  path('<id>/delete', views.delete, name="update" ),
  path('<id>/', views.delete, name="register" ),
  # path('<int:id>/', views.update, name="update")
  path('login/', auth_views.LoginView.as_view(template_name="polls/login.html"), name="login"),
]