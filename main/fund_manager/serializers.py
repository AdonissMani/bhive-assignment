from rest_framework import serializers
from .models import Portfolio, MutualFund

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
        request = self.context['request']
        validated_data['myuser'] = request.user
        return super().create(validated_data)
 