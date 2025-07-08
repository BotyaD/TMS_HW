import csv

import json

"""
 1, 2, 3
"""

#1 Определить количество городов в файле

with open("city_list.json", "r", encoding="utf-8") as f:
    city_list = json.load(f)
    total_city = len(city_list)
    print(f"Количество городов равна: {total_city}")



#2 Создать словарь где ключем является код страны, а значением города

cordinate_country_list = {}
with open("city_list.json", "r", encoding="utf-8") as f:
    city_list = json.load(f)
    city_dict = {value["id"]: value["name"] for value in city_list}
    print(city_dict)






#3 Подсчитать количетво городов в северном и в южном полушарии

with open("city_list.json", "r", encoding="utf-8") as file:
    city_list = json.load(file)
north_hem = 0
south_hem = 0
for city in city_list:
  if city["coord"]["lat"] < 0:
      north_hem += 1

  elif city["coord"]["lat"] > 0:
      south_hem += 1

print(f"Количество городов в северном полушарии: {north_hem}")
print(f"Количество городов в южном полушарии: {south_hem}")


#4 Перевести в CSV файл данные по городам (кординаты представить
# в виде строки значений через запятую

with open("city_list.json", "r", encoding="utf-8") as file:
    json_file = json.load(file)

with open("scv_file.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Country", "Coordinates"])
    for city in json_file:
        try:
            cordinates = city["coord"]["lat"],city["coord"]["lon"]

            writer.writerow([city.get("name", ""), city.get("country", ""), cordinates])
        except KeyError:
            continue

#5 Создать другой json файл, в который сохранить только города одной выбранной страны
with open("city_list.json", "r", encoding="utf-8") as f:
    city_list = json.load(f)

ve_country = [city for city in city_list if city.get("country") == "VE"]

with open("one_city.json", "w", encoding="utf-8") as f:
   json.dump(ve_country, f)