import os
import subprocess

import schedule
import requests

from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


from selenium import webdriver

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def name():
    def test_basic_options():
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)

        driver.quit()

    driver = webdriver.Firefox();

    driver.get("https://ru.tradingview.com/symbols/USDTUSD/?exchange=CRYPTO");

    timeout = 1

    try:
        element_present = EC.presence_of_element_located((By.ID, 'main'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")


    driver.save_screenshot(r'C:\test\test1\image.png');


    driver.quit()


    gauth = GoogleAuth()

    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:

        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:

        gauth.Refresh()
    else:

        gauth.Authorize()

    gauth.SaveCredentialsFile("mycreds.txt")

    drive = GoogleDrive(gauth)



    path = r'C:\test\test'


    for x in os.listdir(path):

    	f = drive.CreateFile({'title': x})
    	f.SetContentFile(os.path.join(path, x))
    	f.Upload()


    	f = None


############################################################
############################################################
############################################################
############################################################
############################################################

    def test_basic_options():
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)

        driver.quit()

    driver = webdriver.Firefox();

    driver.get("https://ru.tradingview.com/symbols/USDRUB_TOM/?exchange=MOEX");

    timeout = 1

    try:
        element_present = EC.presence_of_element_located((By.ID, 'main'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")


    driver.save_screenshot(r'C:\testt\img.png');


    driver.quit()


    gauth = GoogleAuth()

    gauth.LoadCredentialsFile("mycreds1.txt")
    if gauth.credentials is None:

        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:

        gauth.Refresh()
    else:

        gauth.Authorize()

    gauth.SaveCredentialsFile("mycreds1.txt")

    drive = GoogleDrive(gauth)



    path = r'C:\testt'


    for x in os.listdir(path):

    	f = drive.CreateFile({'title': x})
    	f.SetContentFile(os.path.join(path, x))
    	f.Upload()


    	f = None


def main():
    schedule.every(20).seconds.do(name)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
