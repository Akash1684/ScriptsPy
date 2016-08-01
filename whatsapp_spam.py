#NOTE: for this script to work you have to first sign-in on Whatsapp web using QR code

from splinter import Browser

browser = Browser()
browser.visit('https://web.whatsapp.com/')
input('press enter to continue')   #to make sure page is completely loaded 
count=20;

friend_list=["friend 1","friend 2","friend 3"]  #Whatsapp names of friends

for friend in friend_list:
    xp='//span[contains(text(),'+friend+')]'
    chat = browser.find_element_by_path(xp)
    chat.click()
    elem1 = browser.find_elements_by_class_name('input')
    for i in range(1,count):
        elem1[1].send_keys('Whatsapp has expired')   #text to send
        browser.find_element_by_class_name('send-container').click()
