from django.urls import path

from .views import HelloAPIView

urlpatterns = [
    path("greeting/", HelloAPIView.as_view(), name="greeting")
]
