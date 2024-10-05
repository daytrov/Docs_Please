import requests
import json
import random
from datetime import datetime


#Функция get_data получает всю инфу и человеке с сайта
#Ее не нужно вызывать отдельно, вызывается через first_iteration
def get_data():
    response = requests.get('https://api.randomdatatools.ru/')
    data = response.json()
    return data


#Заранее подготовленный лист с инфой о человеке.
#Пустой до первой итерации
personal_dict = {
    'LastName': '',
    'FirstName': '',
    'FatherName': '',
    'Gender': '',
    'DateOfBirth': '',
    'YearsOld': '',
    'Phone': '',
    'Login': '',
    'Password': '',
    'Email': '',
    'Address': '',
    'Country': '',
    'Region': '',
    'City': '',
    'Street': '',
    'Apartment': '',
    'House': '',
    'PasportNum': '',
    'PasportCode': '',
    'PasportOtd': '',
    'PasportDate': '',
    'inn_fiz': '',
    'snils': '',
    'oms': '',
    'bankBIK': '',
    'bankCorr': '',
    'bankINN': '',
    'bankNum': '',
    'bankClient': '',
    'bankCard': '',
    'bankDate': '',
    'bankCVC': '',
}


#Функция convert_personal_info заполняет пустой лист (или заполненый инфой о прошлом человеке) инфой с api
#Отельно вызывать не нужно, вызывается функцией get_info если новый человек, или first_iteration если первая итерация
#Если потом будет нужно менять какую-либо инфу о человеке, делать это тут
def convert_personal_info(data):
    personal_dict["LastName"] = data["LastName"]
    personal_dict["FirstName"] = data["FirstName"]
    personal_dict["FatherName"] = data["FatherName"]
    personal_dict["DateOfBirth"] = data["DateOfBirth"]
    personal_dict["YearsOld"] = data["YearsOld"]
    personal_dict["Phone"] = data["Phone"]
    personal_dict["Login"] = data["Login"]
    personal_dict["Password"] = data["Password"]
    personal_dict["Email"] = data["Email"]
    personal_dict["Address"] = data["Address"]
    personal_dict["Country"] = data["Country"]
    personal_dict["Region"] = data["Region"]
    personal_dict["City"] = data["City"]
    personal_dict["Street"] = data["Street"]
    personal_dict["Apartment"] = data["Apartment"]
    personal_dict["House"] = data["House"]
    personal_dict["PasportNum"] = data["PasportNum"]
    personal_dict["PasportCode"] = data["PasportCode"]
    personal_dict["PasportOtd"] = data["PasportOtd"]
    personal_dict["PasportDate"] = data["PasportDate"]
    personal_dict["inn_fiz"] = data["inn_fiz"]
    personal_dict["snils"] = data["snils"]
    personal_dict["oms"] = data["oms"]
    personal_dict["bankBIK"] = data["bankBIK"]
    personal_dict["bankCorr"] = data["bankCorr"]
    personal_dict["bankINN"] = data["bankINN"]
    personal_dict["bankNum"] = data["bankNum"]
    personal_dict["bankClient"] = data["bankClient"]
    personal_dict["bankCard"] = data["bankCard"]
    personal_dict["bankDate"] = data["bankDate"]
    personal_dict["bankCVC"] = data["bankCVC"]
    return personal_dict


#Функция get_info основная функция в файле, возвращает лист с инфой о человеке.
#Аргумент iteration:
#True - получаем данные с api о новом человеке
#False - работает с данными о старом человеке, который уже загружен в personal_dict
def get_info(iteration):
    if iteration:
        data = get_data()
        convert_personal_info(data)
        return personal_dict
    else:
        return personal_dict


#Функция first_iteration нужна для первого прогона программы, ее следует вызвать один раз перед началом работы.
#Возможно ее потом удалим за ненадобностью
def first_iteration():
    data = get_data()
    convert_personal_info(data)
