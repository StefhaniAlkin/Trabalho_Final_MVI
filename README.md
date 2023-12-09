## Trabalho_Final_MVI
Trabalho final do *Módulo IV: Versionamento e Arquivos de Marcação* da Ada Tech.

### Descrição

Neste trabalho, desenvolvemos uma ferramenta para receber um arquivo `CSV` de produtos vendidos pela Amazon e gerar arquivos de saída em três formatos diferentes: `XML`, `JSON` e `YAML`. 

**Equipe:**

:small_blue_diamond: Camila - https://github.com/7cami

:small_blue_diamond: Gisele - https://github.com/xlSilva

:small_blue_diamond: Nathália - https://github.com/martinsnathalia

:small_blue_diamond: Sabrina - https://github.com/abyss-child

:small_blue_diamond: Stefhani - https://github.com/StefhaniAlkin


**Programa:** Quero Ser Data Analytics

**Linguagem de programação:** Python

**Aquivos:**

* `entrada.csv`: exemplo de entrada para teste

* `csv_to_xml.py`: script que converte `CSV` para `XML`

* `csv_to_json.py`: script que converte `CSV` para `JSON`

* `csv_to_yaml.py`: script que converte `CSV` para `YAML`

* `gerador_nf.py`: script que fornece o arquivo de saída no formato indicado pelo usuário

* `saida.xml`: saída em `XML` para o exemplo

* `saida.json`: saída em `JSON` para o exemplo

* `saida.yaml`: saída em `YAML` para o exemplo


### Como executar

Para instalar as bibliotecas necessárias, escreva, na linha de comando no terminal, o código
```
pip install -r requirements.txt
```

Para testar a ferramenta desenvolvida, execute apenas o script principal `gerador_nf.py` dentro da pasta contendo todos os arquivos (Trabalho_Final_MVI). 
A saída desejada é configurada através do parâmetro `formato`.

Por exemplo, para obter o arquivo em `JSON` escreva, na linha de comando, o código

```
python gerador_nf.py --formato=json
```