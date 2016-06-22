
import os
import time
from splinter import Browser

browser = Browser()
browser.visit('https://internet.iitb.ac.in/index.php')
time.sleep(3)
print("OPENED")
user = browser.find_by_name('uname')
user.fill(########)
pas = browser.find_by_name('passwd')
pas.fill(#########)

browser.find_by_name('button').click()

os.system('netsh wlan start hostednetwork')

#os.system('netsh wlan stop hostednetwork')

