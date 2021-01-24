import json
from re import search
import requests
import webbrowser
if __name__ == '__main__':
    #url = "https://datos.gob.es/apidata/catalog/dataset/l01200697-coronavirus-poblacion-afectada?_sort=title&_pageSize=10&_page=0"
    url = "https://datos.gob.es/apidata/catalog/dataset?_sort=title&_pageSize=10&_page=0"
    response = requests.get(url, verify=False)


    def item_generator(json_input, lookup_key):
        if isinstance(json_input, dict):
            for k, v in json_input.items():
                if k == lookup_key and (search('covid', v) or search('covid', k)) and search('.csv', v):
                    yield v
                else:
                    yield from item_generator(v, lookup_key)
        elif isinstance(json_input, list):
            for item in json_input:
                yield from item_generator(item, lookup_key)


    if(response.status_code == 200):
        content = response.content
        parsed_content = json.loads(content)


for i in item_generator(parsed_content, 'accessURL'):
    webbrowser.open(i)


full = "Stackabuse"
sub = "tack"

dict = {
    "covid1": "si",
    "covid2": "no",
    "estonoescovaid" : "tontooo"
}

for k,v in dict.items():
    if search('covid', k):
        print(v)

if search(sub, full):
    print("si")
else:
    print("no")

a = "hola.csv"


