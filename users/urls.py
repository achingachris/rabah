from django.urls import path

from .views import (
    UserProfileView,
    ChangeUserPassword,
    CustomLogout,
    MemberUserProfileUpdateView,
)

app_name = "user"
urlpatterns = [
    path("user_profile/", UserProfileView.as_view(), name="user_profile"),
    path(
        "member_profile_edit/<str:profile_id>/",
        MemberUserProfileUpdateView.as_view(),
        name="member_profile_edit",
    ),
    path(
        "change_user_password/",
        ChangeUserPassword.as_view(),
        name="change_user_password",
    ),
    path("custom_logout", CustomLogout.as_view(), name="custom_logout"),
]
