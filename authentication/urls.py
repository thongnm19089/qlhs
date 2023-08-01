from django.urls import path

from authentication import  views

urlpatterns = [
 path('', views.home, name ="home"),
 path('signup', views.signup, name ="signup"),
 path('signin', views.signin, name ="signin"),
 path('signout', views.signout, name ="signout"),
 path('add', views.ADD, name = "add"),
 path('update/<str:id>', views.update, name="update" ),
 path('delete/<str:id>', views.delete, name="delete" ),
 
]