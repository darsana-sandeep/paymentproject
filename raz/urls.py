from django.urls import path

from raz import views

urlpatterns = [
    path('',views.payment)
]