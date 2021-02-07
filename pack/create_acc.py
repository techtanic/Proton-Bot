import os
import time

from colorama import Fore, init
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pack.functions import *

init(convert = True)

def create_account(driver, email, x_i, y_i):

    print(Fore.CYAN+"Creating Account...........", Fore.WHITE)
    if email == '': 
        email = input("Please enter email: \t")

    print('\n\n\n')
    
    try:
        new_tab(driver)
        driver.switch_to.window(driver.window_handles[1])
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
        randuser = random_user()
        for i in randuser:
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
            driver.close()
            os._exit(1)

        human_move(driver, '//*[@id="emailVerification"]',x_i,y_i)
        input_value(driver, '//*[@id ="emailVerification"]', email)
        time.sleep(.5)
        human_move(driver, '//*[@id="verification-panel"]/form[1]/div[1]/div[2]/button', x_i, y_i)

    except:
        try:
            driver.close()
        except:
            pass
    return randuser, randpwd
