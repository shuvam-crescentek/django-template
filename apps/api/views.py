from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import views, viewsets
from rest_framework.response import Response

from apps.api.serializers import UserSerializer
from apps.data_access.models import User


# Create your views here.
class HomeApiView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        return Response({"message": "api home"})


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        obj = get_object_or_404(self.queryset, pk=kwargs.get("pk"))
        serializer = UserSerializer(obj)
        return Response(serializer.data)

    """
    def create(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass
    """
