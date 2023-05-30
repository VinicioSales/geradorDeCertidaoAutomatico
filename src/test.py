from backEnd.modules.funcs.funcs import *
from unidecode import unidecode

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
        