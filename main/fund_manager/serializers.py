from rest_framework import serializers
from .models import Portfolio, MutualFund


class MutualFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutualFund
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    mutual_fund = serializers.SlugRelatedField(
        queryset=MutualFund.objects.all(),
        slug_field='scheme_code'
    )

    class Meta:
        model = Portfolio
        fields = ['mutual_fund', 'units', 'investment_date']
        read_only_fields = ['investment_date']

    def create(self, validated_data):
        # Get the user and mutual fund from the validated data
        user = self.context['request'].user
        mutual_fund = validated_data['mutual_fund']
        units = validated_data['units']

        # Check if a portfolio entry already exists for the user and mutual fund
        portfolio, created = Portfolio.objects.get_or_create(
            myuser=user,
            mutual_fund=mutual_fund,
            defaults={'units': units}
        )

        if not created:
            # If the portfolio already exists, update the units
            portfolio.units += units
            portfolio.save()

        return portfolio
