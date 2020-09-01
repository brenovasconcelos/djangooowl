from django.urls import path, re_path
from . import views

urlpatterns = [
    path("allusers/", views.AllUsersView.as_view(), name="all-users"),
    re_path("user/(?P<user_id>[^/]*)/", views.UserView.as_view(), name="one-user"),
]