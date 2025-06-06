from datetime import datetime

def parse_russian_dates(raw):
    """
        Преобразует список строк с датами на русском языке (например, '1 Января 2025 года, среда') в список словарей
        с отформатированной датой ('01.01.2025') и соответствующим днём недели ('среда').
        Используется для стандартизации формата дат, полученных с сайта, и упрощения дальнейшей обработки данных.
    """
    month_map = {
        "января": "01", "февраля": "02", "марта": "03", "апреля": "04",
        "мая": "05", "июня": "06", "июля": "07", "августа": "08",
        "сентября": "09", "октября": "10", "ноября": "11", "декабря": "12"
    }
    weekday_map = {
        "Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
        "Friday": 4, "Saturday": 5, "Sunday": 6
    }
    date_part = raw.lower().replace("года", "").split(",")[0]
    parts = date_part.strip().split(" ")
    day = parts[0].zfill(2)
    month = month_map[parts[1]]
    year = parts[2]
    formatted_date = f"{day}.{month}.{year}"
    weekday_en = datetime.strptime(formatted_date, "%d.%m.%Y").strftime("%A")
    weekday_ru = weekday_map[weekday_en]
    return {
        "date": formatted_date,
        "weekday": weekday_ru
    }
