from django.contrib import admin
from django.urls import path, include
from mysite.views import home_page
from polling.views import list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blogging.urls")),
    path("polling/", include("polling.urls")),
]
