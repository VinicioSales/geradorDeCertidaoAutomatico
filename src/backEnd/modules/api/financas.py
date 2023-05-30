import json
import requests
from backEnd.modules.data.credenciais import credenciais

app_key = credenciais['app_key']
app_secret = credenciais['app_secret']
url = 'https://app.omie.com.br/api/v1/financas/contareceber/'

def listar_contas_receber(pagina: int):
    """
    Função para listar as contas a receber.
    
    Args:
        pagina (int): O número da página a ser consultada.

    Returns:
        A resposta da requisição feita à API.

    """
    payload = json.dumps({
                            "call": "ListarContasReceber",
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