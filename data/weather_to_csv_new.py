import json
import csv


input_file = 'data/Saint-Petersburg24.09.06.json'

# Открываем JSON-файл и загружаем данные
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Задаем дату для фильтрации
target_date = "2024-09-08"

# Извлекаем данные
hourly_data = []
for entry in data.get("forecasts", []):
    # Проверяем дату
    if entry.get("date") == target_date:
        for hour in entry.get("hours", []):
            hourly_data.append({
                "hour": hour.get("hour"),
                "condition": hour.get("condition"),
                "pressure_mm": hour.get("pressure_mm"),
            })

# Записываем данные в CSV-файл
output_file = "weather_"+target_date+".csv"
with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["hour", "condition", "pressure_mm"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(hourly_data)

print(f"Данные записаны в файл {output_file}")
