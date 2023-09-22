import json
import requests
from modules.data.credenciais import credenciais

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
                                            "apenas_importado_api": "N",
                                            "ordenar_por": "DATA_VENCIMENTO"
                                        }
                                    ]
                        })
    headers ={
                'Content-Type': 'application/json'
            }
    response = requests.request("POST", url, headers=headers, data=payload)

    return response

def listar_contas_receber_cliente(cpf_cnpj: str, pagina: int):
    """
    Função para listar as contas a receber de um cliente.
    
    Args:
        pagina (int): O número da página a ser consultada.
        cpf_cnpj (str): cfp ou cnpj do cliente.

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
                                            "apenas_importado_api": "N",
                                            "filtrar_por_cpf_cnpj": cpf_cnpj,
                                            "ordenar_por": "DATA_VENCIMENTO"
                                        }
                                    ]
                        })
    headers ={
                'Content-Type': 'application/json'
            }
    response = requests.request("POST", url, headers=headers, data=payload)

    return response