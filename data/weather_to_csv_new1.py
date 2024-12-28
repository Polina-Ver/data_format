import json
import csv

def process_weather_json(json_file, csv_file, target_date):
    """
    Обрабатывает JSON-файл с погодными данными для указанной даты и сохраняет их в CSV-файл

    param json_file     входной JSON-файл
    param csv_file      выходной CSV-файл
    param target_date   Дата в формате 'ГГГГ-ММ-ДД', на которую нужно извлечь данные
    """
    try:
        # Чтение данных из JSON-файла
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Извлечение данных для указанной даты
        hourly_data = []
        for forecast in data.get("forecasts", []):
            if forecast.get("date") == target_date:
                for hour in forecast.get("hours", []):
                    hourly_data.append({
                        "hour": hour.get("hour"),
                        "condition": hour.get("condition"),
                        "pressure_mm": hour.get("pressure_mm"),
                    })

        if not hourly_data:
            print(f"Данные для даты {target_date} не найдены.")
            return

        # Запись данных в CSV
        with open(csv_file, mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["hour", "condition", "pressure_mm"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(hourly_data)

        print(f"Данные для {target_date} успешно записаны в файл {csv_file}.")
    except FileNotFoundError:
        print(f"Файл {json_file} не найден.")
    except json.JSONDecodeError:
        print("Ошибка при чтении JSON-файла. Проверьте его формат.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


input_json = "data/Saint-Petersburg24.09.06.json"  # Входной файл
target_date = "2024-09-08"  # Дата
output_csv = f"weather_{target_date}.csv"  # Выходной файл
process_weather_json(input_json, output_csv, target_date)
