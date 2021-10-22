from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('list/', MyListView.as_view(), name="list"),
]
