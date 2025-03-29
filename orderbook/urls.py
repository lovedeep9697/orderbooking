from rest_framework import routers
import orderbook.api as api
from django.urls import path, include

router = routers.DefaultRouter()
# End point to create Tokens for the system
router.register(r"tokens", api.TokenViewSet)
# End point to do all order related tasks like view all orders
router.register(r"orders", api.OrderViewSet, basename="orders")
# End point to fetch all executed trades
router.register(r"trades", api.TradeViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
