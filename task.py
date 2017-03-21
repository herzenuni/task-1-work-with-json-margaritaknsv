# Импортируем модуль json

import json

# pprint позволяет в понятном для человека виде форматировать 'сложные' структуры данных 

import pprint

filename = 'data.json'

try:

    with open(filename, encoding='utf-8') as data_file:
        
        data = json.load (data_file)
		
		#используем модуль json и метод для считывания данных: (data_file)

except FileNotFoundError:

    print("Файл не найден! Файл должен называться: {}".format(filename))
    
    status = 'Файл не найден'

pprint(data)

# Выводим в форматированном виде поля: company, email, phone, address

for tmp in data:
    print("Company: {}".format(tmp["company"]))
    print("E-mail: {}".format(tmp["email"]))
    print("Phone: {}".format(tmp["phone"]))
    print("Address: {}".format(tmp["address"]))