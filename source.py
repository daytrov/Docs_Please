import BD_api
import podpis
import fontstyle

BD_api.first_iteration()

abitur_info = BD_api.get_info(False)
lier_abitur_info = BD_api.liar()
print(abitur_info["FirstName"])
print(abitur_info["DateOfBirth"])
print(abitur_info["YearsOld"])
print(abitur_info["PasportDate"])
print(lier_abitur_info["FirstName"])
print(fontstyle.apply(f"{abitur_info["LastName"]} {abitur_info["FirstName"][0]}.{abitur_info["FatherName"][0]}", 'ITALIC'))
#podpis.get_img(abitur_info["FirstName"], abitur_info["LastName"], abitur_info["FatherName"])
