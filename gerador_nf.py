import argparse
from csv_to_json import *
from csv_to_xml import *
from csv_to_yaml import *

parser = argparse.ArgumentParser("Projeto Final: Gerador/conversor de notas fiscais")
parser.add_argument("--formato", dest='formato', help="O formato desejado da nota fiscal. Opções disponíveis: XML, JSON e YAML.", type=str, choices=['xml', 'json', 'yaml'])
parser.add_argument("--pdf", dest='pdf', help="Indica se um pdf deve ser gerado ou não", type=bool, default=False)
args = parser.parse_args()

if args.formato == 'json':
    csv_to_json(csv_filename, output_filename)

if args.formato == 'xml':
    csv_to_json(csv_filename, output_filename)

if args.formato == 'yaml':
    csv_to_json(csv_filename, output_filename)

    