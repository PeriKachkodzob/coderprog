import requests
from time import sleep
from bs4 import BeautifulSoup

url = 'https://api.telegram.org/bot'
token = '499486375:AAFQh1Vgh-Zxf2Qe7ovFoUK_61sdt53Ue7c'
chat_id = 385220023

prevList = []

html = requests.get('https://coderprog.com/')
soup = BeautifulSoup(html.text, 'html.parser')
tags = soup.findAll('article', {'class':['latestPost excerpt ', 'latestPost excerpt last']})

for tag in tags:
    title = tag.find('div', {'style':'text-align:center;'}).get_text()
    prevList.append(title)

def sendMessage(title, urlCover):
    params = {'chat_id': chat_id, 'photo': urlCover, 'caption':title}
    response = requests.post(url + token + '/sendPhoto', data=params)
    return response

def main():
    global prevList
    while True:
        lastList = []
        html = requests.get('https://coderprog.com/')
        soup = BeautifulSoup(html.text, 'html.parser')
        tags = soup.findAll('article', {'class':['latestPost excerpt ', 'latestPost excerpt last']})
        for tag in tags:
            title = tag.find('div', {'style':'text-align:center;'}).get_text()
            lastList.append(title)
            if title not in prevList:
                urlCover = 'https://coderprog.com/' + tag.img['src']
                sendMessage(title, urlCover)
        prevList = lastList
        sleep(3600)

main()
