from django.urls import path
from polling.views import list_view

urlpatterns = [
    path("", list_view),
    path("poll/<int:poll_id>")
]

