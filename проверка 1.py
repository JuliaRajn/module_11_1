import pandas as pd

# Читаем данные из CSV-файла
data = pd.read_csv('data.csv', sep=';')  #  Указываем точку с запятой как разделитель

# Выводим первые 5 строк DataFrame
print(data.head())

# Фильтруем данные по столбцу "Имя"
filtered_data = data[data["Имя"] == "Иван"]
print(filtered_data)

# Группируем данные по столбцу "Город" и выводим средний возраст по городам
grouped_data = data.groupby("Город")["Возраст"].mean()
print(grouped_data)


