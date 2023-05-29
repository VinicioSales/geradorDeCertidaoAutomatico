from backEnd.funcs import geradores
from backEnd.modules import caminhos

data_emissao = '03/05/2023'
data_validade = '02/06/2023'
codigo_verificacao = 'AM3MJACNYMW'

#geradores.gerar_certidao_positiva(cnpj_cpf='00930940000180', inscricao_municipal='00930940000180', razao_social='LOJA MACONICA BENJAMIM PEREIRA MASCARENHAS Nº 2847', endereco='RUA GETULIO VARGAS, 78 - null - CENTRO', municipio_uf='Prado / BA')
#geradores.gerar_certidao_negativa(cnpj_cpf='00930940000180', inscricao_municipal='00930940000180', razao_social='LOJA MACONICA BENJAMIM PEREIRA MASCARENHAS Nº 2847', endereco='RUA GETULIO VARGAS, 78 - null - CENTRO', municipio_uf='Prado / BA', data_emissao=data_emissao, data_validade=data_validade, codigo_verificacao=codigo_verificacao)

data_emissao = '28/02/2023'
data_validade = '30/03/2023'
codigo_verificacao = 'MTMYMDIZ'
cnpj_cpf = '22067400525'
inscricao_municipal = '22067400525'
razao_social = 'LOJA MACONICA 02 DE JULHO Nº 1421*'
endereco = 'RUA Jogo do Carneiro, 157 - null - Saúde'
municipio_uf = 'Salvador / BA'
geradores.gerar_certidao_positiva_negativa(cnpj_cpf=cnpj_cpf, inscricao_municipal=inscricao_municipal, razao_social=razao_social, endereco=endereco, municipio_uf=municipio_uf, data_emissao=data_emissao, data_validade=data_validade, codigo_verificacao=codigo_verificacao)
import os
os.startfile(f'{caminhos.resultado}/CERTIDAO POSITIVA COM EFEITO NEGATIVO.pdf')
