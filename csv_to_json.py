import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    with open(json_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)

csv_filename = "entrada.csv"
json_filename = "saida.json"

csv_to_json(csv_filename, json_filename)