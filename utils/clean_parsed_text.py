import re

def clean_parsed_text(value: str):
    if not value or not isinstance(value, str):
        return value
    match = re.search(r'-?\d+', value)
    if match:
        return int(match.group())
    else:
        return value.strip()