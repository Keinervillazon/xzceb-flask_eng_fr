import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

language_translator.set_disable_ssl_verification(True)

def englishToFrench(englishText):
    #write the code here
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    return englishText

