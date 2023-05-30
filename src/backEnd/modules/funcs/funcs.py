import json
from backEnd.modules.api.clientes import *
from backEnd.modules.api.financas import *

#NOTE - get_codigo_clientes
def get_codigo_clientes():
    """
    Função para obter os códigos dos clientes.

    A função itera sobre várias páginas para recuperar os códigos dos clientes utilizando a função `listar_clientes`.

    Returns:
        Um dicionário contendo os códigos dos clientes, onde a chave é a razão social e o valor é o código.

    """
    dict_codigo_cliente_omie = {}
    pagina = 1
    total_de_paginas = 1
    while pagina <= total_de_paginas:
        response = listar_clientes(pagina=pagina)
        response = response.json()
        clientes_cadastro = response['clientes_cadastro']
        total_de_paginas = int(response['total_de_paginas'])
        for cliente in clientes_cadastro:
            codigo_cliente_omie = cliente['codigo_cliente_omie']
            razao_social = cliente['razao_social']
            dict_codigo_cliente_omie[razao_social] = codigo_cliente_omie
        pagina = pagina + 1

    return dict_codigo_cliente_omie

#NOTE - get_contas_receber_clientes
def get_contas_receber_clientes():
    dict_contas_receber_clientes = {}
    pagina = 1
    total_de_paginas = 1
    while pagina <= total_de_paginas:
        response = listar_contas_receber(pagina=pagina)
        response = response.json()
        conta_receber_cadastro = response['conta_receber_cadastro']
        for conta_receber in conta_receber_cadastro:
            codigo_cliente_fornecedor = conta_receber['codigo_cliente_fornecedor']
            if codigo_cliente_fornecedor == '6550693870':
                continue
            if codigo_cliente_fornecedor in dict_contas_receber_clientes:
                dict_contas_receber_clientes[codigo_cliente_fornecedor] += 1
            else:
                dict_contas_receber_clientes[codigo_cliente_fornecedor] = 1
        pagina = pagina + 1

    return dict_contas_receber_clientes
