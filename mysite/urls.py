from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from mysite.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name='home'),
    path("", include("blogging.urls")),
    path('blogging/', include("blogging.urls")),
    path("polling/", include("polling.urls")),
    path('login/', views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(next_page='/'), name="logout"),
    path('auth/', include('social_django.urls', namespace='social')),
]
