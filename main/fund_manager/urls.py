

from django.urls import path
from .views import FetchFundListView, FetchFundView, PortfolioCreateView, PortfolioListView

urlpatterns = [
    path('load/funds/<str:fund_family>/', FetchFundListView.as_view(), name='fetch_open_ended_funds'),
    path('funds/', FetchFundView.as_view(), name='fetch_all_funds'),
    path('portfolio/', PortfolioCreateView.as_view(), name='add-portfolio'),
    path('portfolios/', PortfolioListView.as_view(), name='list-portfolios'),
]
