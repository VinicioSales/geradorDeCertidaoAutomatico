from funcs import geradores

data_emissao = '03/05/2023'
data_validade = '02/06/2023'
codigo_verificacao = 'AM3MJACNYMW'

#geradores.gerar_certidao_positiva(cnpj_cpf='00930940000180', inscricao_municipal='00930940000180', razao_social='LOJA MACONICA BENJAMIM PEREIRA MASCARENHAS Nº 2847', endereco='RUA GETULIO VARGAS, 78 - null - CENTRO', municipio_uf='Prado / BA')
geradores.gerar_certidao_negativa(cnpj_cpf='00930940000180', inscricao_municipal='00930940000180', razao_social='LOJA MACONICA BENJAMIM PEREIRA MASCARENHAS Nº 2847', endereco='RUA GETULIO VARGAS, 78 - null - CENTRO', municipio_uf='Prado / BA', data_emissao=data_emissao, data_validade=data_validade, codigo_verificacao=codigo_verificacao)
import os
os.startfile('CERTIDAO NEGATIVA.pdf')
