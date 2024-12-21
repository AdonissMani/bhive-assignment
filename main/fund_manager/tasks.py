from celery import shared_task
from .models import MutualFund, Portfolio
from .utils import fetch_open_ended_schemes

@shared_task
def update_portfolios_and_navs():
    # Fetch all mutual funds and their NAVs
    all_funds = MutualFund.objects.all()
    data = fetch_open_ended_schemes(None, 'Open')

    if not data:
        print("Failed to fetch NAV data.")
        return

    # Update NAVs for all MutualFunds
    for fund in all_funds:
        if f"{fund.name}" in data:
            fund.nav = data[f"{fund.name}"]['Net_Asset_Value']
            fund.save()
            print(f"Updated NAV for {fund.name}")
        else:
            print(f"Failed to update NAV for {fund.name}")

    # Update user portfolios
    portfolios = Portfolio.objects.select_related('mutual_fund')
    for portfolio in portfolios:
        if portfolio.mutual_fund.nav:
            current_value = portfolio.units * portfolio.mutual_fund.nav
            print(
                f"Updated portfolio for user {portfolio.myuser}: "
                f"{portfolio.units} units of {portfolio.mutual_fund.name} -> Current Value: {current_value}"
            )
        else:
            print(f"Failed to update portfolio for {portfolio.myuser}: {portfolio.mutual_fund.name}")
