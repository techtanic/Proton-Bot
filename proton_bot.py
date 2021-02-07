import os
import platform

import undetected_chromedriver as uc
from colorama import init

from pack.create_acc import create_account
from pack.functions import calculate_move
from pack.temp_gen import temp_mail
from pack.verify import verification

init(convert = True)

driver_path = "default"


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

options = uc.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
options.add_argument('--log-level=3')
driver = uc.Chrome(options = options)
driver.maximize_window()
print("- . -.-. .... - .- -. .. -.-.")


x_i, y_i = calculate_move()
randuser, randpwd = create_account(driver, temp_mail(driver), x_i, y_i)
verification(driver, randuser, randpwd)
