from django.urls import path
from . import views

urlpatterns = [
    path('submit/expence/$', views.submit_expence),
]