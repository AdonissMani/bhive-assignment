import base64
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from fund_manager.models import MutualFund, Portfolio
from rest_framework.authtoken.models import Token

from user.models import CustomUser

class FundTests(APITestCase):

    def setUp(self):
        # Create a user using the custom user model
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        
        self.auth = 'testuser:testpassword'        
        # Add some test mutual funds
        MutualFund.objects.create(
            fund_family="Aditya Birla Sun Life Mutual Fund",
            name="Test Fund 1",
            nav=10.5,
            scheme_code="12345",
            is_open_ended=True
        )
        MutualFund.objects.create(
            fund_family="Aditya Birla Sun Life Mutual Fund",
            name="Test Fund 2",
            nav=12.5,
            scheme_code="67890",
            is_open_ended=True
        )

        # adding on portfolio
        Portfolio.objects.create(
            myuser=self.user,
            mutual_fund=MutualFund.objects.get(scheme_code="12345"),
            units=10
        )

        # Create a Basic Auth token for the user
        self.auth = base64.b64encode(b'testuser:testpassword').decode('utf-8')

    def test_add_portfolio(self):
        url = '/api/v1/broker/portfolio/'
        data = {'mutual_fund': '12345', 'units': 10}
        response = self.client.post(url, data, HTTP_AUTHORIZATION='Basic ' + self.auth)
        # Verify the response status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Ensure the portfolio was added
        self.assertEqual(Portfolio.objects.count(), 1)

    def test_list_all_funds(self):
        self.url = '/api/v1/broker/funds/'
        response = self.client.get(self.url, HTTP_AUTHORIZATION='Basic ' + self.auth)
        
        # Ensure the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure the data contains all funds
        data = response.data
        print(f'all funds : {data}')
        self.assertGreater(len(data), 0)  #

    def test_view_portfolio(self):
        url = '/api/v1/broker/portfolios/'
        response = self.client.get(url, HTTP_AUTHORIZATION='Basic ' + self.auth)
        
        # Verify the response status
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Ensure 'portfolios' is in the response data
        self.assertIn('portfolios', response.data)
