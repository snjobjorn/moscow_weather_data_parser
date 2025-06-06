import re

def clean_parsed_text(value: str):
    """
        Функция очищает строки от сопутствующих символов и конвертирует в int. Актуально для данных о температуре, где, например,
        встречается символ "°". Строки же остаются строками.
    """
    if not value or not isinstance(value, str):
        return value
    match = re.search(r'-?\d+', value)
    if match:
        return int(match.group())
    else:
        return value.strip()