from typing import List

from polaris.integrations import RailsIntegration
from polaris.models import Transaction
from django.db.models import QuerySet

class MyRailsIntegration(RailsIntegration):
    def poll_pending_deposits(self, pending_deposits: QuerySet) -> List[Transaction]:
        return list(pending_deposits)

    def execute_outgoing_transaction(self, transaction: Transaction):
        transaction.amount_fee = 0
        transaction.status = Transaction.STATUS.completed
        transaction.save()
