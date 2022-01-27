import imp
from django.urls import path, include
from .views import Coupans

urlpatterns=[
    path('', Coupans.as_view())
]