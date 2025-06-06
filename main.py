import os
import json
import time
import random
from datetime import datetime, timedelta
from utils import get_page_content, get_weather_data

def main():
    result = dict()
    os.makedirs("result", exist_ok=True)
    current = datetime(year=2024, month=1, day=1)
    end = datetime(year=2024, month=12, day=31)
    while current <= end:
        day_str = current.strftime("%d-%m")
        url = f"https://pogoda1.ru/moscow/{day_str}/"
        print(f"[INFO] Загружаем {url}")
        try:
            page_soup = get_page_content.get_page_content(url)
            weather = get_weather_data.get_weather_from_page(page_soup)
            result = result | weather
        except Exception as e:
            print(f"[ERROR] Не удалось обработать {url}: {e}")
        # time.sleep(1)
        current += timedelta(days=1)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"result/result_{timestamp}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"[DONE] Данные сохранены в {output_path}")

if __name__ == "__main__":
    main()