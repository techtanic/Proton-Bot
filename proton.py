import os
import platform

from colorama import init
from selenium import webdriver

from pack.auto_driver import autodriver
from pack.create_acc import create_account
from pack.functions import calculate_move

init(convert = True)

driver_path = "default"

os_name = platform.system()
if os_name == "Linux":
    clear_cmd = 'clear'
    arch = 'linux64'

if os_name == "Windows":
    clear_cmd = 'cls'
    arch = 'win32'

if os_name == "Darwin":
    clear_cmd = 'clear'
    arch = 'mac64'

def clear():
    return os.system(clear_cmd)

if autodriver(arch):

    clear()

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--ignore-certificate-error")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(options = options)
    print("- . -.-. .... - .- -. .. -.-.")


    x_i, y_i = calculate_move()
    create_account(driver, x_i, y_i)

else:
    print("Could not complete, because the old driver is in use.")

