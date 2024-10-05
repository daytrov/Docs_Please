import base64
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import PIL
from PIL import Image
import os

#Фукнция get_img получает изображение подписи с сайта
#На вход получает:
#first_name - имя человека
#last_name - фамилия человека
#middle_name - отчество человека
#Передавать аргументы в функция только в таком порядке
def get_img(first_name, last_name, middle_name):
    driver = webdriver.Chrome()
    driver.get("https://podpis-online.ru/")
    time.sleep(2)
    driver.find_element(By.NAME, "name").send_keys(first_name)
    driver.find_element(By.NAME, "surname").send_keys(last_name)
    driver.find_element(By.NAME, "middle").send_keys(middle_name)
    driver.find_element(By.XPATH, "//div[@id='GetSignature']").click()
    time.sleep(2)
    canvas = driver.find_element(By.ID, "Signature_1")
    image_data = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
    with open("not_converted_podpis.png", "wb") as f:
        f.write(base64.b64decode(image_data))
    driver.quit()
    convert_img()

#Функция convert_img удаляет белый фон у изображения и сохраняет его с названием podpis.png
#Эту функцию не нужно вызавать, она запускается через get_img
#После сохранения подписи без фона, удаляет старое изображение с фоном
def convert_img():
    img = Image.open("not_converted_podpis.png")
    img = img.convert("RGBA")
    pixels = img.getdata()
    new_pix = []
    for i in pixels:
        if i[0] > 140 and i[1] > 140 and i[2] > 140:
            new_pix.append((255, 255, 255, 0))
        else:
            new_pix.append(i)
    img.putdata(new_pix)
    img.save("podpis.png", "PNG")
    os.remove("D:/PyCharmProjects/Docs_Please/not_converted_podpis.png")
