import re
import os
from funcs.geradores import *
from unidecode import unidecode
from modules.api.clientes import *
from modules.api.financas import *
from modules.api.google import *



#NOTE - get_nome_clientes_func
def get_nome_clientes_func():
    """
    Retorna uma lista com os nomes dos clientes cadastrados.

    Returns:
        list: Uma lista contendo os nomes dos clientes cadastrados.
    """

    lista_nome_clientes = []
    pagina = 1
    total_de_paginas = 1
    while pagina <= total_de_paginas:
        response = listar_clientes(pagina=pagina)
        response = response.json()
        clientes_cadastro = response['clientes_cadastro']
        total_de_paginas = int(response['total_de_paginas'])
        for cliente in clientes_cadastro:
            lista_nome_clientes.append(cliente['razao_social'])
        pagina = pagina + 1

    return lista_nome_clientes

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
            dados_cliente['cnpj_cpf'] =  cliente['cnpj_cpf']
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
    codigo_categoria_divida_ativa = '1.01.79'

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
            categorias = conta_receber['categorias']
            for categoria in categorias:
                codigo_categoria = categoria['codigo_categoria']
                if codigo_categoria == codigo_categoria_divida_ativa:
                    dic_conta_atrasada['divida_ativa'] = True
                    break
                else:
                    dic_conta_atrasada['divida_ativa'] = False
            if status_titulo == "ATRASADO":
                dic_conta_atrasada['atrasada'] = True
                dict_contas_receber_atrasadas_clientes[codigo_cliente_fornecedor] = dic_conta_atrasada
            elif codigo_cliente_fornecedor not in dict_contas_receber_atrasadas_clientes:
                dic_conta_atrasada['atrasada'] = False
                dict_contas_receber_atrasadas_clientes[codigo_cliente_fornecedor] = dic_conta_atrasada
        
        pagina = pagina + 1

    return dict_contas_receber_atrasadas_clientes

#NOTE - remover_caracteres_especiais
def remover_caracteres_especiais(cpf_cnpj):
    """
    Remove caracteres especiais de um CPF ou CNPJ.

    Args:
        cpf_cnpj (str): CPF ou CNPJ a ser processado.

    Returns:
        str: CPF ou CNPJ sem caracteres especiais.

    """
    cpf_cnpj = re.sub(r'[^0-9]', '', cpf_cnpj)
    
    return cpf_cnpj

#SECTION - script
def script(dict_dados_clientes, razao_social_pesquisado, dict_codigo_clientes, dict_status_contas_receber_clientes):
    codigo_cliente_omie = None
    codigo_cliente_omie_tupla = None
    atrasada = None

    razao_social_pesquisado = unidecode(razao_social_pesquisado).lower()

    #NOTE - Get codigo_cliente_omie
    for cliente in dict_codigo_clientes.items():
        razao_social = cliente[0]
        razao_social = unidecode(razao_social).lower()
        codigo_cliente_omie = cliente[1]
        if razao_social == razao_social_pesquisado:
            codigo_cliente_omie_pesquisado = codigo_cliente_omie
            break
        else:
            codigo_cliente_omie_pesquisado = None
    
    if codigo_cliente_omie_pesquisado != None:
        #NOTE - Get Atrasada
        for cliente in dict_status_contas_receber_clientes.items():
            codigo_cliente_omie_conta_receber = cliente[0]
            status = cliente[1]
            divida_ativa = status['divida_ativa']
            atrasada = status['atrasada']
            if codigo_cliente_omie_conta_receber == codigo_cliente_omie_pesquisado:
                break
            else: 
                atrasada = None
                divida_ativa = None
        

        for cliente  in dict_dados_clientes.items():
            codigo_cliente_omie_tupla = cliente[0]
            if codigo_cliente_omie_tupla == codigo_cliente_omie_pesquisado:
                dados_cliente = cliente[1]
                razao_social = dados_cliente['razao_social']
                cnpj_cpf = dados_cliente['cnpj_cpf']
                endereco = dados_cliente['endereco']
                endereco_numero = dados_cliente['endereco_numero']
                bairro = dados_cliente['bairro']
                cidade = dados_cliente['cidade']
                endereco_completo = f'{endereco}, Nº {endereco_numero} - {bairro}'
                break
        cnpj_cpf = remover_caracteres_especiais(cnpj_cpf)

        print(f'atrasada: {atrasada}')
        print(f'divida_ativa: {divida_ativa}')

        if atrasada == True:

            #FIXME - REMOVER
            print(f'gerar_certidao_positiva')

            gerar_certidao_positiva(cnpj_cpf=cnpj_cpf, razao_social=razao_social, endereco=endereco, municipio_uf=cidade)
            message = f'{razao_social}:\nGerado certidão positiva'

            
        elif atrasada == False and divida_ativa == False:

            #FIXME - REMOVER
            print(f'gerar_certidao_negativa')

            gerar_certidao_negativa(cnpj_cpf, razao_social=razao_social, endereco=endereco_completo, municipio_uf=cidade)
            message = f'{razao_social}:\nGerado certidão negativa'

            
        elif atrasada == False and divida_ativa == True :
            #FIXME - REMOVER
            print(f'gerar_certidao_positiva_negativa')

            gerar_certidao_positiva_negativa(cnpj_cpf=cnpj_cpf, razao_social=razao_social, endereco=endereco_completo, municipio_uf=cidade)
            message = f'{razao_social}:\nGerado certidão positiva com efeito negativo'

        else:
            message = f'{razao_social}:\nNão encontrado'
            
    else:
        message = 'Cliente  não encontrado'

    return message
#!SECTION

    
