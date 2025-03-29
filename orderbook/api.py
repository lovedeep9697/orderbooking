from rest_framework import permissions, viewsets, mixins, exceptions
import orderbook.models as models
import orderbook.serializers as serializers


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class TokenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows token to be viewed or edited.
    """

    queryset = models.Token.objects.all().order_by("name")
    serializer_class = serializers.TokenSerializer
    # Token creation is only allowed to admin user and all
    # other users should be allowed only read only functionalities.
    permission_classes = [permissions.IsAdminUser | ReadOnly]


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows orders to be viewed or created.
    """

    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        username = self.request.query_params.get("username")
        statuses = self.request.query_params.getlist("status")
        queryset = models.Order.objects.all()
        if statuses is not None:
            queryset.filter(status__in=statuses)
        # While getting orders the we might need to see all orders or only current
        # logged in user orders.
        if username is not None and (
            self.request.user.is_staff or self.request.user.username == username
        ):
            queryset = queryset.filter(user__username=username)
        elif username is not None and self.request.user.username != username:
            raise exceptions.PermissionDenied()
        return queryset


class TradeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = models.Trade.objects.all().order_by("-timestamp")
    serializer_class = serializers.TradeSerializer
    permission_classes = [permissions.IsAuthenticated]
