import json
from unidecode import unidecode
from modules.api.clientes import *
from modules.api.financas import *
from funcs.geradores import *


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

#NOTE - get_dados_clientes
def get_dados_clientes():
    """
    Itera sobre várias páginas para recuperar os dados dos clientes utilizando a função `listar_clientes`.

    Returns:
        Um dicionário contendo os dados dos clientes, onde a chave é a razão social e o valor é um dicionário com os dados do cliente.

    """
    dict_dados_clientes = {}
    pagina = 1
    total_de_paginas = 1
    while pagina <= total_de_paginas:
        response = listar_clientes(pagina=pagina)
        response = response.json()
        clientes_cadastro = response['clientes_cadastro']
        total_de_paginas = int(response['total_de_paginas'])
        for cliente in clientes_cadastro:
            dados_cliente = {}
            dados_cliente['razao_social'] = cliente['razao_social']
            dados_cliente['codigo_cliente_omie'] =  cliente['codigo_cliente_omie']
            dados_cliente['cnpj_cpf'] =  cliente['cnpj_cpf']
            dados_cliente['inscricao_municipal'] =  cliente['inscricao_municipal']
            dados_cliente['endereco'] =  cliente['endereco']
            dados_cliente['endereco_numero'] =  cliente['endereco_numero']
            dados_cliente['bairro'] =  cliente['bairro']
            dados_cliente['cidade'] =  cliente['cidade']

            codigo_cliente_omie = cliente['codigo_cliente_omie']
            dict_dados_clientes[codigo_cliente_omie] = dados_cliente
        pagina = pagina + 1

    return dict_dados_clientes

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

#NOTE - script
def script(dict_dados_clientes, razao_social_pesquisado, dict_codigo_clientes, dict_status_contas_receber_clientes):
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
        atrasada = cliente[1]
        atrasada = atrasada['atrasada']
        if codigo_cliente_omie == codigo_cliente_omie_pesquisado:
            print(f'a_vencer: {atrasada}')
            break
    
    for cliente  in dict_dados_clientes.items():
        print(f'cliente: {cliente}')
        codigo_cliente_omie_tupla = cliente[0]
        print(f'codigo_cliente_omie_tupla: {codigo_cliente_omie_tupla} - codigo_cliente_omie_pesquisado: {codigo_cliente_omie_pesquisado}')
        if codigo_cliente_omie_tupla == codigo_cliente_omie_pesquisado:
            dados_cliente = cliente[1]
            razao_social = dados_cliente['razao_social']
            codigo_cliente_omie = dados_cliente['codigo_cliente_omie']
            cnpj_cpf = dados_cliente['cnpj_cpf']
            inscricao_municipal = dados_cliente['inscricao_municipal']
            endereco = dados_cliente['endereco']
            endereco_numero = dados_cliente['endereco_numero']
            bairro = dados_cliente['bairro']
            cidade = dados_cliente['cidade']
            endereco_completo = f'{endereco}, Nº {endereco_numero} - {bairro}'
            break
    print(f'razao_social: {razao_social}')
    print(f'codigo_cliente_omie: {codigo_cliente_omie}')
    print(f'cnpj_cpf: {cnpj_cpf}')
    print(f'inscricao_municipal: {inscricao_municipal}')
    print(f'endereco: {endereco}')
    print(f'endereco_numero: {endereco_numero}')
    print(f'bairro: {bairro}')
    print(f'cidade: {cidade}')
    print(f'endereco_completo: {endereco_completo}')
    
    #FIXME - REMOVER
    codigo_verificacao = '123'
    data_validade = '31/05/2023'

    if atrasada:
        #FIXME - REMOVER
        print(f'gerar_certidao_negativa')

        gerar_certidao_negativa(cnpj_cpf, inscricao_municipal, razao_social, endereco=endereco_completo, municipio_uf=cidade, data_validade=data_validade, codigo_verificacao=codigo_verificacao)
    if not atrasada:
        #FIXME - REMOVER
        print(f'gerar_certidao_positiva_negativa')
        
        gerar_certidao_positiva_negativa(cnpj_cpf, inscricao_municipal, razao_social, data_validade=data_validade, endereco=endereco_completo, municipio_uf=cidade, codigo_verificacao=codigo_verificacao)


    
