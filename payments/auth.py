
from django.conf import settings
import base64
import requests
import logging

logger = logging.getLogger(__name__)

def get_access_token():
    """
    Fetch the access token from Safaricom API.
    """

    #Safaricom API URL for generating OAuth access token
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    # Retrieve consumer key and secret from Django settings (environment variables)
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET

     # URL for fetching access token
    access_token_url = settings.MPESA_ACCESS_TOKEN_URL

    credentials = f"{consumer_key}:{consumer_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    headers = {
        'Authorization': f'Basic {encoded_credentials}'
    }

     # Make the GET request to the API to fetch the access token
    response = requests.get(api_url, headers=headers)
    json_response = response.json()

     # Check if the response status is 200 (successful)
    if response.status_code == 200:
        access_token = json_response['access_token']
        logger.info(f'Access token fetched successfully: {access_token}')
        return access_token
    else:

     # Log the error if the response is not successful
        logger.error(f'Error fetching access token: {json_response}')
        raise Exception('Error fetching access token')