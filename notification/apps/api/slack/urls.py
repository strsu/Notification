from django.urls import path
from apps.api.slack import views

urlpatterns = [
    path("", views.SlackView.as_view(), name=""),
]
