from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics

import orderbooking.serializers


class CreateUserView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = orderbooking.serializers.UserSerializer

    model = User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = orderbooking.serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = orderbooking.serializers.GroupSerializer
    permission_classes = [permissions.IsAdminUser]
