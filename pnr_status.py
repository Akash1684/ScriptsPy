from twilio.rest import TwilioRestClient
from splinter import Browser
import time
from bs4 import  BeautifulSoup

def textmyself(message):
    sid = "##################"
    token = "####################"
    myNumber = ["#################"]
    twilioNumber = "#################"
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
    msg=getstatus("*****PNR******")
    textmyself(msg)  #send message to mobile
    print(msg)


if __name__ == "__main__": main()
