from splinter import Browser
#import Tkinter
import time

def download_art(title):

    browser = Browser()
    # Visit URL
    url = "http://gen.lib.rus.ec/scimag/index.php"
    browser.visit(url)

    article_title = browser.find_by_name('s')
    article_title.fill(title)

    button = browser.find_by_value('Search!')
    # Interact with elements
    button.click()

    #sleep is use at each step to control the follow between program and internet speed

    time.sleep(10)
    browser.click_link_by_text('Libgen')
    time.sleep(15)
    browser.click_link_by_partial_href('http://gen.lib.rus.ec/scimag/get.php')

    time.sleep(5)
    browser.quit()




def main():

   title=input("ENTER NAME OF ARTICLE")

   k=download_art(title)

   if(k==-1):
       print("Article Not Found!!")
   else:
       print("Requested Article Downloaded!!")


main()