from django.urls import path

from . import views
from django.urls import path
from . import views
  

urlpatterns = [
    path('get/', views.StudentView.as_view()),
    path('hello/', views.HelloView.as_view(), name ='hello'),
]