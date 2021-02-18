import requests
import wget
import zipfile
import os
import platform

def autodriver():

    os_name = platform.system()
    if os_name == "Linux":
        arch = 'linux64'

    if os_name == "Windows":
        arch = 'win32'
        
    if os_name == "Darwin":
        arch = 'mac64'
        
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    download_url = "https://chromedriver.storage.googleapis.com/" + version_number + "/chromedriver_" + arch + ".zip"

    latest_driver_zip = wget.download(download_url,'chromedriver.zip')

    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove(latest_driver_zip)