import typing
import orderbook.models
from collections import deque
from dataclasses import dataclass


@dataclass
class OrderMatch:
    price: float
    quantity: int
    bid_order: orderbook.models.Order
    ask_order: orderbook.models.Order


@dataclass
class OrderQueueEntry:
    price: int
    quantity: int
    order: orderbook.models.Order


class MatchingStrategy:
    """
    This class works as a matching engine for all active bids and asks.
    The matching engine would be running in background and keep matching orders.
    """

    # Function to match orders and return an OrderMatch Object.
    def try_matching(self, bid: OrderQueueEntry, ask: OrderQueueEntry):
        if bid.price >= ask.price:
            return OrderMatch(
                price=bid.price,
                quantity=min(bid.quantity, ask.quantity),
                bid_order=bid.order,
                ask_order=ask.order,
            )

    # This function takes a token and returns the matches from all active orders
    def match(self, token: str) -> typing.List[OrderMatch]:
        bid_orders = orderbook.models.Order.objects.filter(
            token=token, status="open", order_type="bid"
        ).order_by("-price", "timestamp")
        ask_orders = orderbook.models.Order.objects.filter(
            token=token, status="open", order_type="ask"
        ).order_by("price", "timestamp")

        bid_queue = deque(
            [
                OrderQueueEntry(price=order.price, quantity=order.quantity, order=order)
                for order in bid_orders
            ]
        )

        ask_queue = deque(
            [
                OrderQueueEntry(price=order.price, quantity=order.quantity, order=order)
                for order in ask_orders
            ]
        )

        matches = []
        while len(bid_queue) and len(ask_queue):
            bid = bid_queue.popleft()
            ask = ask_queue.popleft()

            # If bid user and ask user are the same then we skip that order.
            if bid.order.user == ask.order.user:
                bid_timestamp = bid.order.timestamp
                ask_timestamp = ask.order.timestamp
                if bid_timestamp > ask_timestamp:
                    ask_queue.appendleft(ask)
                else:
                    bid_queue.appendleft(bid)
                continue

            match = self.try_matching(bid, ask)
            if match is not None:
                remaining_bid = bid.quantity - match.quantity
                remaining_ask = ask.quantity - match.quantity

                if remaining_bid != 0:
                    bid_queue.appendleft(
                        OrderQueueEntry(
                            price=bid.price, quantity=remaining_bid, order=bid.order
                        )
                    )

                if remaining_ask != 0:
                    ask_queue.appendleft(
                        OrderQueueEntry(
                            price=ask.price, quantity=remaining_ask, order=ask.order
                        )
                    )

                matches.append(match)

        return matches
