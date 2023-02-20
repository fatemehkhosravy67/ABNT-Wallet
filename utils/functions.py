from apscheduler.schedulers.background import BackgroundScheduler
from mainwallet.views import CreditViewSet, BalanceViewSet


def start():
    scheduler = BackgroundScheduler()
    # credit = CreditViewSet()
    # debit = DebitViewSet()
    # scheduler.add_job(CreditViewSet, "interval", minutes=10, id="wallet_001", replace_existing=True)
    scheduler.add_job(BalanceViewSet, "interval", minutes=10, id="wallet_001", replace_existing=True)
    scheduler.start()