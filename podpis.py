import base64
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def get_img(first_name, last_name, middle_name):
    driver = webdriver.Chrome()
    driver.get("https://podpis-online.ru/")
    time.sleep(5)
    driver.find_element(By.NAME, "name").send_keys(first_name)
    driver.find_element(By.NAME, "surname").send_keys(last_name)
    driver.find_element(By.NAME, "middle").send_keys(middle_name)
    driver.find_element(By.XPATH, "//div[@id='GetSignature']").click()
    time.sleep(5)
    canvas = driver.find_element(By.ID, "Signature_1")
    image_data = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
    with open("signature.png", "wb") as f:
        f.write(base64.b64decode(image_data))
    driver.quit()
