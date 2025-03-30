from django.core.management.base import BaseCommand
from orderbook.tasks import run_matching_task


class Command(BaseCommand):
    help = "Starts the order matching engine"

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting Order Matching Engine...")
        run_matching_task()
