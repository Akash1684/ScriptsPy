import urllib.request
from bs4 import BeautifulSoup
from gtts import gTTS
import os
import datetime



def fetch_news():
    link = urllib.request.urlopen('https://news.google.co.in/')
    # .co.in will fetch news from India domain
    soup = BeautifulSoup(link, "html.parser")
    news_heads = soup.findAll('div', {'class': 'esc-lead-article-title-wrapper'})

    news_no = 0
    vocal_string = ''

    for ne in news_heads:
        vocal_string = vocal_string + '\n\n' + (str(news_no + 1) + '\n' + ne.find('span', {'class': 'titletext'}).text)
        news_no = news_no + 1
        if (news_no == 6):
            break;
            # fetch only top 6 stories

    return vocal_string


def say(con):
    speech = con

    tts = gTTS(text=speech, lang='en')
    #lang='en' means the bot will precieve text as ENGLISH, incase of HINDI  change it to lang='hi'

    date_today=datetime.datetime.now().date()

    tts.save("E:/news "+str(date_today)+".mp3")
    
    os.startfile("E:/news "+str(date_today)+".mp3")


def main():
    speech=fetch_news()
    say(speech)

main()