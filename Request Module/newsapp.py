import requests
import json


apikey=input("enter your News API Key here : ")

news=input("Enter topic of news : ")

url=(f"https://newsapi.org/v2/everything?q={news}&from=2025-05-19&sortBy=publishedAt&apiKey={apikey}")

r = requests.get(url)
news=json.loads(r.text)

for article in news['articles']:
    print('Author :' , article['author'])
    print('Title : ',article['title'])
    print('Descrption :' ,article['description'])
    print("--------------------------")