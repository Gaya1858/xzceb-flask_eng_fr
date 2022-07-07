"""
This is a IBM final project for python api's. Using IBM's watson translating english to 
frech and frech to english
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator =IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)

def englishtofrench(englishtext):
    """
    @param: annglishText takes string
    @return: string of translated
    """

    #write the code here
    language_translator.set_service_url(url)
    frenchtext = language_translator.translate(text=englishtext,model_id='en-fr')
    
    return frenchtext.get_result()['translations'][0]['translation']

def frenchtoenglish(frenchtext):
    """
    @param: annglishText takes string
    @return: string of translated
    """

    #write the code here
    language_translator.set_service_url(url)
    englishtext = language_translator.translate(text=frenchtext,model_id='fr-en')
    return englishtext.get_result()['translations'][0]['translation']


# print(englishtofrench('hello'))
# print(frenchtoenglish('bonjour'))