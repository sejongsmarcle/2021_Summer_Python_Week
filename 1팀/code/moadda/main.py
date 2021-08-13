import requests
from bs4 import BeautifulSoup
import datetime

from flask import Flask, render_template
app = Flask("MadScrapper")


@app.route("/")
def home():
    url1 = "https://finance.naver.com/news/mainnews.nhn"
    result_naver = requests.get(url1)
    soup_naver = BeautifulSoup(result_naver.text, "html.parser")

    url2 = "https://news.google.com/search?q=%EC%A3%BC%EC%8B%9D&hl=ko&gl=KR&ceid=KR%3Ako"
    result_google = requests.get(url2)
    soup_google = BeautifulSoup(result_google.text, "html.parser")

    dds_n = soup_naver.find_all('dd', {"class": "articleSubject"})
    as_g = soup_google.find_all('h3', {"class": "RD0gLb"})
    # print(as_g)

    article_n = []
    article_g = []

    for dd in dds_n:
        title = dd.find('a').text
        link = dd.find('a')['href']
        link = "https://finance.naver.com/"+link
        article_n.append({'Title': title, 'Link': link})
    print(article_n)

    for a in as_g:
        title = a.find('a').text
        link = a.find('a')['href']
        link = "https://news.google.com/search?q=%EC%A3%BC%EC%8B%9D&hl=ko&gl=KR&ceid=KR%3Ako/"+link
        article_g.append({'Title': title, 'Link': link})
    print(article_g)

    now = datetime.datetime.now()

    return render_template(
        "index.html", articles_n=article_n, articles_g=article_g, num_n=len(article_n), num_g=len(article_g), nowDate=now.strftime('%Y-%m-%d')
    )


app.run(host="0.0.0.0")
