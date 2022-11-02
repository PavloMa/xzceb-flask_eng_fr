"""
Translation module.
English - French and
French - English
"""

#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = "2018-05-01"

key_authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=key_authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text=None):
    """
    Translates English into French
    """

    if english_text is None:
        return ""
    try:
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        #dictonary/array/dictionary: result['translations'][0]['translation']
        french_text = translation["translations"][0]["translation"]
        return french_text
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
        return ""

def french_to_english(french_text=None):
    """
    Translates French into English:
    """

    if french_text is None:
        return ""
    try:
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        english_text = translation["translations"][0]["translation"]
        return english_text
    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
        return ""

"""
JSON format of a translation:
{
  "translations": [
    {
      "translation": "Hola, ¿cómo estás hoy?"
    }
  ],
  "word_count": 7,
  "character_count": 25
}
"""
