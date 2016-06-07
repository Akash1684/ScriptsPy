from twilio.rest import TwilioRestClient
from splinter import Browser
import time
from bs4 import  BeautifulSoup

def textmyself(message):
    sid = "AC2943bced271470a0b31a328d7266bba0"
    token = "34845e7364b55d067fe4b00c75d7585f"
    myNumber = ["+919454028991"]
    twilioNumber = "+12318034148"
    twilioClient=TwilioRestClient(sid,token)
    for num in myNumber:
        twilioClient.messages.create(body=message,from_=twilioNumber,to=num)


def getstatus(pnr):
    browser = Browser()
    url = "http://www.indianrail.gov.in/pnr_Enq.html"
    browser.visit(url)
    time.sleep(5)
    browser.fill("lccp_pnrno1", pnr)
    browser.find_by_name("submit").click()
    time.sleep(2)
    soup = BeautifulSoup(browser.html, "html.parser")
    status = soup.findAll('td', {'class': 'table_border_both'})
    string = ""

    string = "PNR:" + pnr + "," + "TRAIN:" + status[0].text

    string = string + ",DOJ:" + status[2].text.replace(" ", "") + ",CLASS:" + status[7].text.replace(" ", "") + "," + \
             status[3].text.replace(" ", "") + "-" + status[4].text.replace(" ", "")
    string = string + "," + "BOOK:" + status[9].text.replace(" ", "") + ",CUR:" + status[10].text.replace(" ",
                                                                                                          "") + ",FARE:" + \
             status[11].text

    return string


def main():
    msg=getstatus("8647677881")
    textmyself(msg)  #send message to mobile
    print(msg)


if __name__ == "__main__": main()