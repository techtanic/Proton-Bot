import json
import os
import random
import time
from datetime import datetime
from threading import Thread

import requests
from bs4 import BeautifulSoup as bs
from capmonster_python import HCaptchaTaskProxyless
from colorama import Back, Fore,init
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from functions import (exit_iframe, find_id, find_xpath, human_move,
                       input_value, switch_to_iframe, webdriver_options)

init(autoreset=True)

try:
    with open("pb-settings.json") as f:
        settings = json.load(f)
except FileNotFoundError:
    with open("pb-settings.json", "w") as f:
        settings = {"browser": None}
        json.dump(settings, f, indent=4)


def save_settings():
    with open("pb-settings.json", "w") as f:
        json.dump(settings, f, indent=4)


while True:
    if not settings["browser"]:
        settings["browser"] = input("1=Firefox\n2=Chrome\nBrowser: ").lower()
    if settings["browser"] in ("1", "firefox"):
        from selenium.webdriver.firefox.options import Options
        from webdriver_manager.firefox import GeckoDriverManager

        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(),
            options=webdriver_options(Options()),
        )
        break

    if settings["browser"] in ("2", "chrome"):
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager

        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            options=webdriver_options(Options()),
        )
        break
    else:
        print("Invalid option")
        settings["browser"] = None

save_settings()
# - . -.-. .... - .- -. .. -.-.
faker = Faker()


print(Fore.CYAN + "Creating Account...........")
print()
driver.get("https://mail.protonmail.com/create/new?language=en")

username = (
    str(faker.random_int(0, 10))
    + faker.first_name().lower()
    + str(faker.random_int(0, 10))
    + str(faker.random_int(0, 10))
)
'''
switch_to_iframe(driver)
find_id(driver, "username").click()
input_value(find_id(driver, "username"), username)
exit_iframe(driver)
'''
switch_to_iframe(driver)
exit_iframe(driver)
for i in ["class","aria-hidden","style"]:
    driver.execute_script(f'document.querySelector("body > div.app-root > div.ui-prominent.bg-norm.color-norm.h100.flex-no-min-children.flex-nowrap.flex-column.h100.sign-layout-bg.scroll-if-needed > div > div > main > div.sign-layout-main-content > form > div:nth-child(1) > div").removeAttribute("{i}")')

find_id(driver, "username").click()
input_value(find_id(driver, "username"), username)

switch_to_iframe(driver)
find_id(driver, "username").click()
input_value(find_id(driver, "username"), username)
exit_iframe(driver)


password = faker.password().lower()
input_value(find_id(driver, "password"), password)

input_value(find_id(driver, "repeat-password"), password)

find_xpath(driver, "/html/body/div[1]/div[2]/div/div/main/div[2]/form/button").click()


check_error = True
while check_error == True:
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[2]/div/div/main/div[2]/form/button[2]",
                )
            )
        )
        check_error = False
    except:
        print(Fore.RED + "\nUsername error\n")
        print(Fore.LIGHTGREEN_EX + "Solving")

        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        username_path = find_id(driver, "username")
        while username_path.get_attribute("value") != "":
            username_path.send_keys(Keys.BACKSPACE)

        username = (
            str(faker.random_int(0, 10))
            + faker.first_name().lower()
            + str(faker.random_int(0, 10))
            + str(faker.random_int(0, 10))
        )
        input_value(username_path, username)

        driver.switch_to.default_content()

        # driver.switch_to.frame(driver.find_element_by_class_name("bottom"))

        human_move(
            driver,
            find_xpath(
                driver, "/html/body/div[1]/div[2]/div/div/main/div[2]/form/button"
            ),
        )

        print(Fore.LIGHTGREEN_EX + "Maybe solved")
        check_error = True
        time.sleep(0.3)


find_xpath(
    driver, "/html/body/div[1]/div[2]/div/div/main/div[2]/form/button[2]"
).click()

find_xpath(driver, "/html/body/div[4]/dialog/form/footer/button[1]").click()

find_xpath(
    driver, "/html/body/div[1]/div[2]/div/div/main/div[2]/div[2]/div[1]/button"
).click()

try:
    """for label in ["label_0", "label_1"]:
        if find_id(driver, label).text == "Email":
            find_id(driver, label).click()
    else:"""
    find_xpath(driver, "//*[text()='Email']").click()
except Exception as e:
    print(e)
    print(Fore.RED + "Looks like YOU have abused the bot!! Try Again later")
    input("Press enter/return key to exit.")
    driver.close()

domain = ["boximail.com", "zetmail.com"]
email = username + "@" + random.choice(domain)

input_value(find_id(driver, "email"), email)
time.sleep(1.5)
try:
    find_xpath(driver, '//*[@id="key_1"]/button').click()
except:
    find_xpath(driver, '//*[@id="key_0"]/button').click()
"""
check_error = True
while check_error:  # check if domain is blocked
    try:
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="signup"]/div[4]')
        email = word + "@" + random.choice(domain)
        driver.find_element_by_xpath('//*[@id ="emailVerification"]').clear()
        input_value(driver, '//*[@id ="emailVerification"]', email)
        human_move(
            driver,
            '//*[@id="verification-panel"]/form[1]/div[1]/div[2]/button',
            x_i,
            y_i,
        )
        time.sleep(1)
    except:
        check_error = False
        """

print(email)  ###################################


while True:
    try:
        r = requests.get(f"https://getnada.com/api/v1/inboxes/{email}").json()
        uid = r["msgs"][0]["uid"]
        break
    except:
        time.sleep(0.5)

html = requests.get(f"https://getnada.com/api/v1/messages/html/{uid}").content
soup = bs(html, "html5lib")
code = soup.find("code").text


input_value(find_id(driver, "verification"), code)
find_xpath(driver, "/html/body/div[1]/div[2]/div/div/main/div[2]/button[1]").click()


capmonster = HCaptchaTaskProxyless(client_key="ClientKey-Here")
taskId = capmonster.createTask(
    website_key="f99ae21a-1f92-46a4-938e-da6a6afb72ec",
    website_url="https://account-api.protonmail.com/",
)
response = capmonster.joinTaskResult(taskId=taskId)
# response = "dfwefw3fuybferklgriuegeor9pwhhhhhhhhhhhhhhhhhhhh"
try:
    switch_to_iframe(driver)
    element = driver.find_element_by_xpath("//*[contains(@id, 'g-recaptcha-response')]")
    driver.execute_script(f"arguments[0].innerHTML = '{response}';", element)
    element = driver.find_element_by_xpath("//*[contains(@id, 'h-captcha-response')]")
    driver.execute_script(f"arguments[0].innerHTML = '{response}';", element)
    driver.execute_script(f'document.querySelector("#html_element > iframe").setAttribute("data-hcaptcha-response","{response}");')
    exit_iframe(driver)
    #driver.execute_script("$('form').submit();")
    driver.execute_script(f"tokenCallback('{response}')")
except KeyError as e:
    print(e)

time.sleep(1)
for i in range(5):
    find_xpath(driver, "/html/body/div[4]/dialog/form/div/div/footer/button").click()
find_xpath(driver, "/html/body/div[4]/dialog/form/div/div/footer/button[2]").click()

print(username)
print(password)

print(Fore.GREEN + "\nAccount Details.\n")

with open("Accounts.txt", "a") as f:
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M") + "\n")
    f.write(username + "\n")
    f.write(password + "\n")
    f.write("-------------------------------\n")
print(username)
print(password)
