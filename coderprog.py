import requests
from time import sleep
from bs4 import BeautifulSoup

url = 'https://api.telegram.org/bot'
token = '499486375:AAFQh1Vgh-Zxf2Qe7ovFoUK_61sdt53Ue7c'
chat_id = 385220023

headers = []

html = requests.get('https://coderprog.com/')
soup = BeautifulSoup(html.text, 'html.parser')
tags = soup.findAll('h2', {'class':'title front-view-title'})

for tag in tags:
    headers.append(tag.get_text())

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + token + '/sendMessage', data=params)
    return response
    
def main():
    while True:
        html = requests.get('https://coderprog.com/')
        soup = BeautifulSoup(html.text, 'html.parser')
        tags = soup.findAll('h2', {'class':'title front-view-title'})
        for tag in tags:
            header = tag.get_text()
            if header not in headers:
                send_mess(chat_id, header)
                headers.append(header)
        sleep(300)

main()
