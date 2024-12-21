

from django.urls import path
from .views import FundListView, PortfolioCreateView

urlpatterns = [
    path('funds/<str:fund_family>/', FundListView.as_view(), name='fetch_open_ended_funds'),
    path('portfolio/', PortfolioCreateView.as_view(), name='add-portfolio'),
]
