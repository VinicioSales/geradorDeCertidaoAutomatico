import json
import requests
from modules.data.credenciais import credenciais

app_key = credenciais['app_key']
app_secret = credenciais['app_secret']
url = 'https://app.omie.com.br/api/v1/geral/clientes/'

#NOTE - listar_clientes
def listar_clientes(pagina: int):
    """
    Função para listar os clientes.
    
    Args:
        pagina (int): O número da página atual.
        total_de_paginas (int): O número total de páginas.
    
    Returns:
        A resposta da requisição feita à API.

    """
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

    return response
