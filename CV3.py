import json
import csv

my_path = "C:/Users/anton/Downloads/persons.csv"

with open(my_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

json_str = json.dumps(data, indent=4, ensure_ascii=False)

print(json_str)
