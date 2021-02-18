import os
import platform

from colorama import init
from selenium import webdriver

from pack.auto_driver import autodriver
from pack.create_acc import create_account
from pack.functions import calculate_move

init(convert = True)

driver_path = "default"

print("Downloading Chrome Driver")
autodriver()

os_name = platform.system()
if os_name == "Linux":
    clear_cmd = 'clear'

if os_name == "Windows":
    clear_cmd = 'cls'
    
if os_name == "Darwin":
    clear_cmd = 'clear'
    

def clear():
    return os.system(clear_cmd)

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
