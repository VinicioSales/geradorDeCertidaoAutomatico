import re

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

cpf_cnpj = '11.111.111/1111-11'
cpf_cnpj = remover_caracteres_especiais(cpf_cnpj)

print(cpf_cnpj)
