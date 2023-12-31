from funcs.geradores import *
from unidecode import unidecode
from modules.api.google import *
from modules.api.clientes import *
from modules.api.financas import *



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
            codigo_cliente_fornecedor = conta_receber['codigo_cliente_fornecedor']
            if codigo_cliente_fornecedor not in dict_contas_receber_atrasadas_clientes:
                dic_conta_atrasada = {}
                status_titulo = conta_receber['status_titulo']

                if status_titulo == "ATRASADO":
                    dic_conta_atrasada['atrasada'] = True
                    dict_contas_receber_atrasadas_clientes[codigo_cliente_fornecedor] = dic_conta_atrasada
                
                elif status_titulo == "A VENCER":
                    categorias = conta_receber['categorias']
                    for categoria in categorias:
                        codigo_categoria = categoria['codigo_categoria']
                        if codigo_categoria == codigo_categoria_divida_ativa:
                            dic_conta_atrasada['divida_ativa'] = True
                            dic_conta_atrasada["data_vencimento"] = conta_receber["data_vencimento"]
                            dic_conta_atrasada["codigo_lancamento_omie"] = conta_receber["codigo_lancamento_omie"]
                            dict_contas_receber_atrasadas_clientes[codigo_cliente_fornecedor] = dic_conta_atrasada
                            break
        
        pagina = pagina + 1

    return dict_contas_receber_atrasadas_clientes


#SECTION - script
def script(dict_dados_clientes, razao_social_pesquisado, dict_codigo_clientes, dict_status_contas_receber_clientes):
    """
    Realiza um processo de geração de certidão com base nos dados de clientes.

    Args:
        dict_dados_clientes (dict): Um dicionário contendo os dados dos clientes.
        razao_social_pesquisado (str): A razão social do cliente a ser pesquisado.
        dict_codigo_clientes (dict): Um dicionário contendo os códigos dos clientes.
        dict_status_contas_receber_clientes (dict): Um dicionário contendo os status das contas a receber dos clientes.

    Returns:
        str: Uma mensagem informando o resultado do processo de geração de certidão.
    """
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
            divida_ativa = status.get('divida_ativa', False)
            atrasada = status.get('atrasada', None)
            data_vencimento = status.get("data_vencimento", None)
            codigo_lancamento_omie = status.get("codigo_lancamento_omie", None)
            if codigo_cliente_omie_conta_receber == codigo_cliente_omie_pesquisado:
                negativa = False
                break
            else:
                negativa = True
                # atrasada = None
                # divida_ativa = None
        

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


        print(f'atrasada: {atrasada}')
        print(f'divida_ativa: {divida_ativa}')

        if atrasada == True:

            gerar_certidao_positiva(cnpj_cpf=cnpj_cpf, razao_social=razao_social, endereco=endereco, municipio_uf=cidade)
            message = f'{razao_social}:\nGerado certidão positiva'

            
        elif negativa == True:

            gerar_certidao_negativa(cnpj_cpf, razao_social=razao_social, endereco=endereco_completo, municipio_uf=cidade)
            message = f'{razao_social}:\nGerado certidão negativa'

            
        elif divida_ativa == True :
            gerar_certidao_positiva_negativa(cnpj_cpf=cnpj_cpf, razao_social=razao_social, endereco=endereco_completo, municipio_uf=cidade, data_vencimento=data_vencimento)
            message = f'{razao_social}:\nGerado certidão positiva com efeito negativo'

        else:
            message = f'{razao_social}:\nNão encontrado'
            
    else:
        message = 'Cliente  não encontrado'

    return message
#!SECTION

