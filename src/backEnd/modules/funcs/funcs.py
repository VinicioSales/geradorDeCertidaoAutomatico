import json
from modules.api.clientes import *
from modules.api.financas import *
from unidecode import unidecode

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
    """
    A função itera sobre várias páginas para recuperar as contas a receber utilizando a função `listar_contas_receber`.

    Returns:
        Um dicionário onde a chave é o código do cliente fornecedor e o valor
        é um dicionário com informações sobre o status da conta.

    """
    dict_contas_receber_atrasadas_clientes = {}
    dic_conta_atrasada = {}
    pagina = 1
    total_de_paginas = 1
    while pagina <= total_de_paginas:
        response = listar_contas_receber(pagina=pagina)
        response = response.json()
        conta_receber_cadastro = response['conta_receber_cadastro']
        for conta_receber in conta_receber_cadastro:
            dic_conta_atrasada = {}
            codigo_cliente_fornecedor = conta_receber['codigo_cliente_fornecedor']
            status_titulo = conta_receber['status_titulo']
            if status_titulo == "ATRASADO":
                dic_conta_atrasada['atrasada'] = True
                dict_contas_receber_atrasadas_clientes[codigo_cliente_fornecedor] = dic_conta_atrasada
            elif codigo_cliente_fornecedor not in dict_contas_receber_atrasadas_clientes:
                dic_conta_atrasada['atrasada'] = False
                dict_contas_receber_atrasadas_clientes[codigo_cliente_fornecedor] = dic_conta_atrasada
        
        pagina = pagina + 1

    return dict_contas_receber_atrasadas_clientes


def script():
    dict_codigo_clientes =  get_codigo_clientes()
    dict_status_contas_receber_clientes = get_contas_receber_clientes()

    razao_social_pesquisado = 'Aprender Escola de Idiomas'

    razao_social_pesquisado = unidecode(razao_social_pesquisado).lower()

    for cliente in dict_codigo_clientes.items():
        razao_social = cliente[0]
        razao_social = unidecode(razao_social).lower()
        codigo_cliente_omie = cliente[1]
        if razao_social == razao_social_pesquisado:
            codigo_cliente_omie_pesquisado = codigo_cliente_omie
            break
    print(f'codigo_cliente_omie_pesquisado: {codigo_cliente_omie_pesquisado}')

    for cliente in dict_status_contas_receber_clientes.items():
        codigo_cliente_omie = cliente[0]
        a_vencer = cliente[1]
        a_vencer = a_vencer['atrasada']
        if codigo_cliente_omie == codigo_cliente_omie_pesquisado:
            print(a_vencer)
            break
