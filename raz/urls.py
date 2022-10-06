from django.urls import path

from raz import views

urlpatterns = [
    path('',views.payment),
    path('msg',views.messages)
]
9