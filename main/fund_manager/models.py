from django.conf import settings
from django.db import models



class MutualFund(models.Model):
    name = models.CharField(max_length=255)
    fund_family = models.CharField(max_length=255)
    nav = models.FloatField()  # Net Asset Value
    is_open_ended = models.BooleanField(default=True)
    scheme_code = models.CharField(max_length=255)


class Portfolio(models.Model):
    myuser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mutual_fund = models.ForeignKey(MutualFund, on_delete=models.CASCADE)
    units = models.FloatField()
    investment_date = models.DateField(auto_now_add=True)
    scheme_code = models.CharField(max_length=255)

    def current_value(self):
        """Calculate the current value of the investment based on NAV."""
        return self.units * self.mutual_fund.nav

    def __str__(self):
        return f"{self.units} units of {self.mutual_fund.name}"
