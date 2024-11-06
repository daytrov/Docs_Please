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
    'EduName': '',
    'EduDocNum': '',
    'EduRegNumber': '',
    'EduYear': ''
}
liar_personal_dict = {
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
        'EduName': '',
        'EduDocNum': '',
        'EduRegNumber': '',
        'EduYear': ''
    }


#Функция convert_personal_info заполняет пустой лист (или заполненый инфой о прошлом человеке) инфой с api
#Отельно вызывать не нужно, вызывается функцией get_info если новый человек, или first_iteration если первая итерация
#Если потом будет нужно менять какую-либо инфу о человеке, делать это тут
def convert_personal_info(data, dict):
    dict["LastName"] = data["LastName"]
    dict["FirstName"] = data["FirstName"]
    dict["FatherName"] = data["FatherName"]
    dict["DateOfBirth"] = data["DateOfBirth"]
    dict["YearsOld"] = data["YearsOld"]
    dict["Phone"] = data["Phone"]
    dict["Login"] = data["Login"]
    dict["Password"] = data["Password"]
    dict["Email"] = data["Email"]
    dict["Address"] = data["Address"]
    dict["Country"] = data["Country"]
    dict["Region"] = data["Region"]
    dict["City"] = data["City"]
    dict["Street"] = data["Street"]
    dict["Apartment"] = data["Apartment"]
    dict["House"] = data["House"]
    dict["PasportNum"] = data["PasportNum"]
    dict["PasportCode"] = data["PasportCode"]
    dict["PasportOtd"] = data["PasportOtd"]
    dict["PasportDate"] = data["PasportDate"]
    dict["inn_fiz"] = data["inn_fiz"]
    dict["snils"] = data["snils"]
    dict["oms"] = data["oms"]
    dict["bankBIK"] = data["bankBIK"]
    dict["bankCorr"] = data["bankCorr"]
    dict["bankINN"] = data["bankINN"]
    dict["bankNum"] = data["bankNum"]
    dict["bankClient"] = data["bankClient"]
    dict["bankCard"] = data["bankCard"]
    dict["bankDate"] = data["bankDate"]
    dict["bankCVC"] = data["bankCVC"]
    dict["EduName"] = data["EduName"]
    dict["EduDocNum"] = data["EduDocNum"]
    dict["EduRegNumber"] = data["EduRegNumber"]
    dict["EduYear"] = data["EduYear"]
    return dict


#Функция get_info основная функция в файле, возвращает лист с инфой о человеке.
#Аргумент iteration:
#True - получаем данные с api о новом человеке
#False - работает с данными о старом человеке, который уже загружен в personal_dict
def get_info(iteration):
    if iteration:
        data = get_data()
        return convert_personal_info(data, personal_dict)
    else:
        return personal_dict


#Функция first_iteration нужна для первого прогона программы, ее следует вызвать один раз перед началом работы.
#Возможно ее потом удалим за ненадобностью
def first_iteration():
    data = get_data()
    convert_personal_info(data, personal_dict)


def liar():
    data = get_data()
    return convert_personal_info(data, liar_personal_dict)
