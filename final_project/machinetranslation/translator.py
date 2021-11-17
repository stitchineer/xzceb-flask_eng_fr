import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['1oVju8djy47qq1IgPsPHmhbDKPNivsBx7SGZgmrmwLcU']
url = os.environ['https://api.us-south.language-translator.watson.cloud.ibm.com/instances/c4e309fb-a3aa-4ed3-89a6-ec3a56a1ead8']
