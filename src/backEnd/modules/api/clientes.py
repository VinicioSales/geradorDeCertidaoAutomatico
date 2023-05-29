import json
import requests
from modules.data.credenciais import credenciais

app_key = credenciais['app_key']
app_secret = credenciais['app_secret']
url = 'https://app.omie.com.br/api/v1/geral/clientes/'

def listar_clientes():
    pagina = 1
    total_de_paginas = 1
    while pagina <= total_de_paginas:
        payload = json.dumps({
                                "call": "ListarClientes",
                                "app_key": app_key,
                                "app_secret": app_secret,
                                "param":[
                                            {
                                                "pagina": pagina,
                                                "registros_por_pagina": 500,
                                                "apenas_importado_api": "N"
                                            }
                                        ]
                            })
        headers ={
                    'Content-Type': 'application/json'
                }
        response = requests.request("POST", url, headers=headers, data=payload)
        