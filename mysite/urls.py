from django.contrib import admin
from django.urls import path, include
from mysite.views import home_page
from polling.views import list_view


# path("polling/", include("polling.urls")

urlpatterns = [
    path("", home_page),
    path('admin/', admin.site.urls),
    path("polling/", include("polling.urls")),
]
