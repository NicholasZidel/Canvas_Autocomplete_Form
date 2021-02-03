import requests
import ctypes
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def main(link):
    driver.get(link)

    try:
        login = open("Login.txt", "r")  # reads login info from Login.txt

        get_element_buffer(By.ID, "username").send_keys(login.readline()[10:])

        get_element_buffer(By.ID, "password").send_keys(login.readline()[10:])

        login.close()

        driver.switch_to.frame('duo_iframe')

        get_element_buffer(By.TAG_NAME, "button").click()

        driver.switch_to.default_content()

        get_element_buffer(By.ID, "none").click()

        form = get_element_buffer(By.ID, "contact-with-no")
        form.click()
        form.submit()

    except:
        ctypes.windll.user32.MessageBoxW(0, "Didn't work", "Error", 1)


def get_element_buffer(locator, str):
    print (str)
    return WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((locator, str))
    )


if __name__ == '__main__':
    main("https://www.banweb.mtu.edu/owassb/symptom_form.p_form")
