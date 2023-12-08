import csv
import xml.etree.ElementTree as ET

def csv_to_xml(csv_file, xml_file):
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        root = ET.Element('listaDeProdutos')
 
        for row in csv_reader:
            produto = ET.SubElement(root, 'produto')
 
            for key, value in row.items():
                element = ET.SubElement(produto, key)
                element.text = value
 
        tree = ET.ElementTree(root)
        tree.write(xml_file, encoding='utf-8')
        
csv_filename = "entrada.csv"
output_filename = "saida.xml"
    
csv_to_xml(csv_filename, output_filename)