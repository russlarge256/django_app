from django.contrib import admin
from django.urls import path, include
from mysite.views import home_page
from polling.views import list_view

urlpatterns = [
    path("", home_page),
    path('admin/', admin.site.urls),
    path("polling/", include("polling.urls")),
    path("blogging/", include("blogging.urls"))
]
