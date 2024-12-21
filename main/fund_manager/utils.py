from decouple import config
import requests

BASE_URL = "https://latest-mutual-fund-nav.p.rapidapi.com"
RAPIDAPI_KEY = config("RAPID_API_KEY")

def fetch_open_ended_schemes(fund_family, scheme_type):
    url = "https://latest-mutual-fund-nav.p.rapidapi.com/latest"

    querystring = {"Mutual_Fund_Family":"Aditya Birla Sun Life Mutual Fund","Scheme_Type":"Open"}

    headers = {
    	"x-rapidapi-key": "96cc8ae4a2msh6f869e5585e9f75p107f42jsna741c372c4ea",
    	"x-rapidapi-host": "latest-mutual-fund-nav.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return (response.json())
