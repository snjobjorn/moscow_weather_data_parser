import random
import json

def get_random_header():
    with open("data/headers.json", "r", encoding="utf-8") as f:
        headers_list = json.load(f)
    return random.choice(headers_list)