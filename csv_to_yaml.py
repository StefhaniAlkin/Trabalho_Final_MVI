import csv
import yaml

def csv_to_yaml(csv_file, yaml_file):
    data = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    with open(yaml_file, 'w', encoding='utf-8') as yaml_file:
        yaml.dump(data, yaml_file, indent=2)

csv_filename = "entrada.csv"
output_filename = "saida.yaml"

csv_to_yaml(csv_filename, output_filename)