from django.urls import path
from blogging.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name="blogging_index"),
    path('post/<int:post_id>/', detail_view, name="blog_detail"),
]