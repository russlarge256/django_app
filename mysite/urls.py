from django.contrib import admin
from django.urls import path, include
from mysite.views import home_page
from polling.views import list_view
# from blogging.views import list_view


# path("polling/", include("polling.urls")

# then modify urlpatterns as follows:
urlpatterns = [
    path('', include('blogging.urls')),
    # path("", home_page),
    path('admin/', admin.site.urls),
    path("polling/", include("polling.urls")),
    # <-- add this
    #... other included urls
]

# urlpatterns = [
#     # path("", home_page),
#     path('admin/', admin.site.urls),
#     path("polling/", include("polling.urls")),
#     path("blogging/", include("blogging.urls")),
# ]
