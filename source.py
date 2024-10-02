import BD_api
import podpis

BD_api.first_iteration()

abitur_info = BD_api.get_info(False)
print(abitur_info["LastName"])
print(abitur_info["DateOfBirth"])
print(abitur_info["YearsOld"])
print(abitur_info["PasportDate"])
podpis.get_img(abitur_info["FirstName"], abitur_info["LastName"], abitur_info["FatherName"])
