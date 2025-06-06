import random
import json

def get_random_header():
    """
        Функция считывает файл "data/headers.json" (содержащий заголовки запросов) и рандомно выбирает оттуда один из них.
        Предназначена для того, чтобы парсинг с меньшей вероятностью был обнаружен.
    """
    with open("data/headers.json", "r", encoding="utf-8") as f:
        headers_list = json.load(f)
    return random.choice(headers_list)