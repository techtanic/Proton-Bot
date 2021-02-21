import os
import time
from datetime import datetime

from RandomWordGenerator import RandomWord
import requests
from bs4 import BeautifulSoup as bs
from colorama import Fore, init
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pack.functions import *

init(convert = True)

def create_account(driver, x_i, y_i):

    print(Fore.CYAN+"Creating Account...........", Fore.WHITE)
    print()
    word = RandomWord(max_word_size = 7).generate()+str(random.randint(0, 9))+str(random.randint(0, 9))
    word = word.lower()
    driver.get("https://mail.protonmail.com/create/new?language=en")
    
    randpwd = random_pwd()
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
        (By.TAG_NAME, 'iframe')))
    time.sleep(.5)
    
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.ID, 'username'))).click
    time.sleep(.5)
    username = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.ID, 'username')))

    for i in word:
        username.send_keys(i)
        time.sleep(.1)

    driver.switch_to.default_content()

    print(Fore.CYAN+"Please wait\n\n", Fore.WHITE)

    password = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, 'password')))

    for i in randpwd:
        password.send_keys(i)
        time.sleep(.1)
    time.sleep(.5)

    print(Fore.CYAN+"Please wait\n\n", Fore.WHITE)
    input_value(driver, '//*[@id = "passwordc"]', randpwd)
    time.sleep(.5)
    driver.switch_to.frame(driver.find_element_by_class_name("bottom"))
    human_move(driver, '//*[@id = "app"]/div/footer/button', x_i, y_i)
    driver.switch_to.default_content()
    time.sleep(1)

    check_error = True
    while check_error == True:
        try:
            WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class = "modal-footer"]')))
            check_error = False
        except:
            print(Fore.RED+"\nUsername error\n", Fore.WHITE)
            print(Fore.LIGHTGREEN_EX+"Solving", Fore.WHITE)
            randuser = random_user()

            driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
            while username.get_attribute('value') != '':
                username.send_keys(Keys.BACKSPACE)

            randuser = random_user() 

            for i in randuser:
                username.send_keys(i)
                time.sleep(.1)

            driver.switch_to.default_content()
            time.sleep(.5)
            driver.switch_to.frame(driver.find_element_by_class_name("bottom"))
            
            human_move(driver, '//*[@id = "app"]/div/footer/button', x_i, y_i)

            driver.switch_to.default_content()

            print(Fore.LIGHTGREEN_EX+"Maybe solved", Fore.WHITE)
            check_error = True
            time.sleep(.3)

    human_move(driver, '//*[@id = "confirmModalBtn"]', x_i, y_i)
    time.sleep(1)

    try:
        human_move(driver, '//*[@id="verification-panel"]/div[3]/label/div', x_i, y_i)
        human_move(driver, '//*[@id="verification-panel"]/div[2]/label/div', x_i, y_i)
    except:
        print(Fore.RED+"Looks like YOU have abused the bot!! Try Again later", Fore.WHITE)
        input("Press enter/return key to exit.")
        driver.close()
        return

    human_move(driver, '//*[@id="emailVerification"]',x_i,y_i)

    domain = ['boximail.com']
    email = word + "@" + random.choice(domain)
    input_value(driver, '//*[@id ="emailVerification"]', email)
    human_move(driver, '//*[@id="verification-panel"]/form[1]/div[1]/div[2]/button', x_i, y_i)

    check_error = True
    while check_error:  #check if domain is blocked
        try:
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="signup"]/div[4]')
            email = word + "@" + random.choice(domain)
            driver.find_element_by_xpath('//*[@id ="emailVerification"]').clear()
            input_value(driver, '//*[@id ="emailVerification"]', email)       
            human_move(driver, '//*[@id="verification-panel"]/form[1]/div[1]/div[2]/button', x_i, y_i)
            time.sleep(1)
        except:
            check_error = False
    while True:
        try:
            uid = requests.get(f"https://getnada.com/api/v1/inboxes/{email}").json()
            uid = uid["msgs"][0]["uid"]
            break
        except:
            time.sleep(1)
            pass
    html = requests.get(f"https://getnada.com/api/v1/messages/html/{uid}").content
    soup = bs(html,"html5lib")
    code = soup.find("code").text
    
    human_move(driver, '//*[@id="codeValue"]',x_i, y_i)
    code_input = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type = "text"]')))
    for i in code:
        code_input.send_keys(i)
        time.sleep(.1)

    human_move(driver, '//*[@id="verification-panel"]/p[3]/button', x_i, y_i) # Complete setup btn
    time.sleep(1)

    human_move(driver, '//*[@id="confirmModalBtn"]',x_i,y_i)

    for _ in range(0, 3):
        human_move(driver, '//*[@id="pm_wizard"]/div/div[5]/button[1]',x_i,y_i)
        time.sleep(.5)
    human_move(driver, '//*[@id="pm_wizard"]/div/div[5]/button[2]',x_i,y_i)

    print(Fore.GREEN+"\nAccount Details.\n", Fore.WHITE)

    username = "Username: " + word
    password = "Password: " + randpwd
    with open("Accounts.txt", 'a') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M")+"\n")
        f.write(username+"\n")
        f.write(password+"\n")
        f.write("-------------------------------\n")
    print(username)
    print(password)

    return
