import time

from colorama import Fore, init

from pack.functions import find_xpath
import random

init(convert = True)

'''- . -.-. .... - .- -. .. -.-.'''
def temp_mail(driver):
    
    print(Fore.CYAN+"\n\n Generating a temp-mail......\n", Fore.WHITE)
    print('\n ')
    driver.get('https://getnada.com/')
    time.sleep(1)
    find_xpath(driver, '//*[@id="__layout"]/div/div/div[2]/nav/div/div/ul[1]/li[1]/button').click() # Add more inboxes

    find_xpath(driver, '//*[@id="__layout"]/div/div/div[2]/nav/div[2]/div/div/div/form/div/div[2]/select').click() # Click domains 

    find_xpath(driver, '//*[@id="__layout"]/div/div/div[2]/nav/div[2]/div/div/div/form/div/div[2]/select/option[{}]'.format(random.randint(1,12))).click() # select zetmail Domian (12)

    find_xpath(driver, '//*[@id="__layout"]/div/div/div[2]/nav/div[2]/div/div/div/form/button').click() # Click Add now


    print(Fore.CYAN+"Please wait\n\n", Fore.WHITE)
    email = find_xpath(driver,'//*[@id="__layout"]/div/div/div[2]/div/div[1]/div/div/p/span[1]/a/button').text
    return email
