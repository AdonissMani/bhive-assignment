from rest_framework.permissions import IsAuthenticated
from fund_manager.models import MutualFund, Portfolio
from .utils import fetch_open_ended_schemes
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MutualFundSerializer, PortfolioSerializer
from rest_framework import generics

class FetchFundListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, fund_family):
        # Get the fund family from query params
        if not fund_family:
            return Response({"error": "Fund family is required"}, status=400)

        # Call the RapidAPI utility function, passing the authenticated user
        data = fetch_open_ended_schemes(fund_family, request.user)
        print("saving in DB")
        for fund in data:
            MutualFund.objects.create(
                fund_family = fund['Mutual_Fund_Family'],
                name = fund['Scheme_Name'],
                nav = fund['Net_Asset_Value'],
                scheme_code = fund['Scheme_Code'],
                is_open_ended = True

            )
        return Response(data, status=200)

class FetchFundView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MutualFund.objects.all()
    serializer_class = MutualFundSerializer


class PortfolioCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PortfolioSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PortfolioListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PortfolioSerializer

    def list(self, request, *args, **kwargs):
        portfolios = Portfolio.objects.filter(myuser=request.user)
        serializer = self.serializer_class(portfolios, many=True)
        return Response({'portfolios': serializer.data}, status=status.HTTP_200_OK)


