import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['V1ZIsl0vdvTLH3vuod6GCLvwkeONIXOPNeqb8QkuQd_6']
url = os.environ['https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/fe2c0dea-2835-4c51-82d7-b478fb27feb1']
version = '2021-05-17'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    translation = language_translator.translate(
        text=englishText,
        source='en',
        target='fr'
    ).get_result()

    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    translation = language_translator.translate(
        text=frenchText,
        source='fr',
        target='en'
    ).get_result()

    englishText = translation['translations'][0]['translation']
    return englishText
    