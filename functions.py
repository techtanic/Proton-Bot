import random
import string
import time
from bs4 import element

import numpy as np
import scipy.interpolate as si
from colorama import init
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def webdriver_options(options):
    options.headless = True
    options.add_argument("--ignore-certificate-error")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--log-level=3")
    return options


def webdriver_options(options):
    # options.headless = True
    options.add_argument("--ignore-certificate-error")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument("--log-level=3")
    return options


def new_tab(driver):
    driver.execute_script("window.open('','_blank');")


def switch_to_iframe(driver):
    
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.TAG_NAME, "iframe"))
    )
    iframe = driver.find_element_by_tag_name("iframe")
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    return iframe
    
def exit_iframe(driver):
    driver.switch_to.default_content()
    

def find_xpath(driver, xpath):
    element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    time.sleep(0.4)
    return element


def find_id(driver, id):
    element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, id)))
    time.sleep(0.4)
    return element


def input_value(element, value):
    for i in value:
        element.send_keys(i)
        time.sleep(0.1)
    time.sleep(0.3)


def calculate_move():
    points = [[6, 2], [3, 2], [0, 0], [0, 2]]
    points = np.array(points)
    x = points[:, 0]
    y = points[:, 1]
    t = range(len(points))
    ipl_t = np.linspace(0.0, len(points) - 1, 100)
    x_tup = si.splrep(t, x, k=1)
    y_tup = si.splrep(t, y, k=1)
    x_list = list(x_tup)
    xl = x.tolist()
    x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]
    y_list = list(y_tup)
    yl = y.tolist()
    y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]
    x_i = si.splev(ipl_t, x_list)
    y_i = si.splev(ipl_t, y_list)
    return x_i, y_i


def human_move(driver, element):
    x_i, y_i = calculate_move()
    action = ActionChains(driver)
    action.move_to_element(element)
    action.perform()
    c = 4
    i = 0
    for mouse_x, mouse_y in zip(x_i, y_i):
        action.move_by_offset(mouse_x, mouse_y)
        action.perform()
        time.sleep(0.05)
        i += 1
        if i == c:
            break
    element.click()
