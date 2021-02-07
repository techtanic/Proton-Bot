import undetected_chromedriver as uc 

uc.TARGET_VERSION = 85
driver = uc.Chrome()
driver.get('https://distilnetworks.com')