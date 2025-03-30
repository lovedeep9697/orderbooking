from orderbook.engine import MatchingStrategy
from background_task import background
from datetime import datetime
from orderbook.models import Trade


# @background(schedule=timedelta(seconds=1))
def run_matching_task():
    matches = MatchingStrategy().match(token=1)
    trades = []
    for match in matches:
        trades = Trade.objects.create(
            price=match.price,
            quantity=match.quantity,
            timestamp=datetime.now(),
            bid_order=match.bid_order,
            ask_order=match.ask_order,
        )
