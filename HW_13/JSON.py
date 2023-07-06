# Використайте прикріплений файл json та прочитайте його за допомогою модулю json.
import json
from pprint import pprint

with open('sample2.json', 'r', encoding='utf-8') as f:
    json = json.load(f)
    pprint(json)
