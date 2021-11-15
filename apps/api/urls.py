from django.urls import path

from apps.api.views import HomeApiView, UserApiViewSet

urlpatterns = [
    path("", HomeApiView.as_view(), name="api-home"),
    path(
        "users/",
        UserApiViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="users-list",
    ),
    path(
        "users/<int:pk>",
        UserApiViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="users-list",
    ),
]
