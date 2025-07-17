from django.urls import path

from api.views import *
from .views import *

urlpatterns = [
    path("", BookAPIView.as_view(),name="books")
]
