import requests
import wget
import zipfile
import os

def autodriver(arch):   
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    download_url = "https://chromedriver.storage.googleapis.com/" + version_number + "/chromedriver_" + arch + ".zip"

    latest_driver_zip = wget.download(download_url,'chromedriver.zip')

    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        try:
            zip_ref.extractall()
        except PermissionError:
            return False
    os.remove(latest_driver_zip)
    return True