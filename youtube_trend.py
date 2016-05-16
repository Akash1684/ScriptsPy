from bs4 import BeautifulSoup
import urllib.request
from http import cookies
from splinter import Browser
import time
from selenium import webdriver

def main():
    r = urllib.request.urlopen('https://www.youtube.com/feed/trending')
    soup = BeautifulSoup(r, "html.parser")

    trend_box = soup.find('li', {'class': 'expanded-shelf-content-item-wrapper'})

    title = trend_box.find('h3', {'class': 'yt-lockup-title'}).find('a').text

    cook = cookies.SimpleCookie()        #to check whether the trending video is already downloaded or not
    for a in trend_box.find_all('a', href=True):
        link = a['href']
        break;

    try:
        if cook["title"].value == title:
            print("ALREADY DOWNLOADED THIS VIDEO")
        else:
            cook["title"] = title
            cook['title']['expires'] = 12 * 30 * 24 * 60 * 60
            print("DOWNLOADING : " + title)
            download(link)
    except KeyError:
        cook["title"]=title
        cook['title']['expires'] = 12 * 30 * 24 * 60 * 60
        print("DOWNLOADING : " + title)
        download(link)


def download(link):
    browser = Browser()
    browser.visit('https://www.ssyoutube.com'+link)
    time.sleep(22)
    print("OPENED")
    browser.click_link_by_text('Download')


main()




