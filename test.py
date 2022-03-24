import wikipedia
from random import randint
import rstr
import json
import requests


# JSON Parser for Obscene.json
def randomRecord():
    with open('obscene.json', "r", encoding='utf-8') as fp:
        data = json.load(fp)
        words = data["RECORDS"]
        random_index = randint(0, len(words) - 1)
        return words[random_index]['word']


# wikipedia GET request API
wiki = wikipedia.page(randomRecord())
text = wiki.content
# print(text)

# Generate random 10 digit number (phone number)
num = rstr.digits(10)

# loop to send Texts
headers = {
    'Authorization': 'Bearer #',
    'Content-Type': 'application/json'
}

body = {
    'from': num,
    'to': '+NUMBER',
    'body': text
}

response = requests.post('https://us.sms.api.sinch.com/xms/v1/#/batches', headers=headers, data=body)
