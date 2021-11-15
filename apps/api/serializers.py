from rest_framework.serializers import ModelSerializer
from apps.data_access.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "phone",
            "is_active",
            "created",
            "updated",
        ]
