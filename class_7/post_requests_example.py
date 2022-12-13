import requests

url = 'https://libretranslate.de/translate'

phrase = input("Please type a sentence: ")
source_language = input("What language is the phase? ")
target_language = input("What language would like to translate it to? ")

params = {'q':phrase, 'source': source_language, 'target': target_language}

response = requests.post(url, params=params)


print(response.url)
print(response.text)
py_obj = response.json()
translated_text = py_obj['translatedText']
print(f"{phrase} -> {translated_text}")
