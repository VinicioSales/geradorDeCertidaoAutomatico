from PIL import Image
from static.variaveis import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet


pdfmetrics.registerFont(TTFont('font1', font_principal))
pdfmetrics.registerFont(TTFont('font1_bold', font_principal_bold))
styles = getSampleStyleSheet()
style = styles["Normal"]

#NOTE - gerar_certidao_positiva
def gerar_certidao_positiva(cnpj_cpf: str, inscricao_municipal: str, razao_social: str, endereco: str, municipio_uf: str):
    """
    Gera uma certidão positiva de débitos.

    Esta função utiliza as informações fornecidas para gerar um documento PDF contendo a certidão positiva de débitos.

    Parâmetros:
    - cnpj_cpf: str - O número do CNPJ ou CPF do solicitante.
    - inscricao_municipal: str - O número da inscrição municipal do solicitante.
    - razao_social: str - O nome ou razão social do solicitante.
    - endereco: str - O endereço do solicitante.
    - municipio_uf: str - O município e UF (Unidade Federativa) do solicitante.
    """
    cnv = canvas.Canvas('CERTIDAO POSITIVA.pdf', pagesize=A4)
    
    #NOTE - logo
    img = Image.open(logo)
    width, height = img.size
    escala = 0.2
    width = width * escala
    height = height * escala
    cnv.drawImage(logo, x=25, y=730, width=width, height=height)

    #NOTE - Borda
    largura, altura = A4
    cnv.setLineWidth(1.1)
    cnv.roundRect(20, 20, largura-40, altura-40, 10, stroke=1, fill=0)
    cnv.line(x1=20, y1=100, x2=575, y2=100)

    #NOTE - Cabeçalho
    x = 120
    y = 805
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='ESTADO  BAHIA')
    cnv.setFont('font1_bold', 12)
    cnv.drawString(x=x, y=y-15, text='GRANDE ORIENTE DO BRASIL - BAHIA')
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='SECRETARIA DE FINANCAS GOB-BA')
    cnv.setFont('font1_bold', 10)
    cnv.drawString(x=x, y=y-45, text='RUA JOGO DO CARNEIRO, 157 - SAÚDE - 40.045-040')
    cnv.drawString(x=x, y=y-60, text='CNPJ: 14670178000154')
    img = Image.open(qr_code)
    width, height = img.size
    escala = 0.07
    width = width * escala
    height = height * escala
    cnv.drawImage(qr_code, x=495, y=730, width=width, height=height)

    #NOTE - Título
    x = 300
    y = 700
    cnv.setFont('font1_bold', 12)
    cnv.drawCentredString(x=x, y=y, text='CERTIDÃO POSITIVA DE DÉBITOS')
    cnv.drawCentredString(x=x, y=y-14, text='RELATIVOS ÀS TAXAS DO GRANDE ORIENTE DO BRASIL - BA')

    #NOTE - Dados
    x = 35
    y = 605
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='CNPJ/CPF:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+145, y=y, text=cnpj_cpf)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-15, text='INSCRIÇÃO MUNICIPAL:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+145, y=y-15, text=inscricao_municipal)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='NOME / RAZÃO SOCIAL:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+145, y=y-30, text=razao_social)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-45, text='ENDEREÇO:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+145, y=y-45, text=endereco)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-60, text='MUNICIPIO / UF:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+145, y=y-60, text=municipio_uf)

    #NOTE - Texto
    x = 35
    y = 490
    cnv.setFont('font1', 12)
    cnv.drawString(x=x, y=y, charSpace=0.3, text='As informações disponíveis na Secretaria de Finanças do Grande Oriente do Brasil – Bahia /')
    cnv.drawString(x=x, y=y-15, charSpace=0.45, text='GOB-BA, sobre a A R L S acima identificada são insuficientes para a emissão de Certidão')
    cnv.drawString(x=x, y=y-30, charSpace=0.3, text='Negativa ou Positiva Com Efeito Negativo de Débitos.')
    x = 290
    y = 375
    cnv.drawCentredString(x=x, y=y, text='Existem débitos!')
    cnv.drawCentredString(x=x, y=y-15, text='Para consultar sua situação fiscal solicite seu extrato.')

    #NOTE - Rodapé
    x = 300
    y = 70
    cnv.setFont('font1_bold', 8)
    cnv.drawCentredString(x=x, y=y, text='E-mail:financeiro.goeb@gmail.com Site: Telefone: (71) 32410420')
    cnv.drawCentredString(x=x, y=y-13, text='Autenticidade do documento sujeita a verificação.')
    cnv.drawCentredString(x=x, y=y-23, text='Acesse: https://gob-ba.link3.com.br/l3-grp/Servicos.html para verificação.')

    cnv.save()

#NOTE - gerar_certidao_negativa
def gerar_certidao_negativa(cnpj_cpf: str, inscricao_municipal: str, razao_social: str, endereco: str, municipio_uf: str, data_emissao:str, data_validade:str, codigo_verificacao: str):
    """
    Gera uma certidão negativa de débitos.

    Esta função utiliza as informações fornecidas para gerar um documento PDF contendo a certidão negativa de débitos.

    Parâmetros:
    - cnpj_cpf: str - O número do CNPJ ou CPF do solicitante.
    - inscricao_municipal: str - O número da inscrição municipal do solicitante.
    - razao_social: str - O nome ou razão social do solicitante.
    - endereco: str - O endereço do solicitante.
    - municipio_uf: str - O município e UF (Unidade Federativa) do solicitante.
    - data_emissao: str - A data de emissão da certidão.
    - data_validade: str - A data de validade da certidão.
    - codigo_verificacao: str - O código de verificação da certidão.
    """
    cnv = canvas.Canvas('CERTIDAO NEGATIVA.pdf', pagesize=A4)
    
    #NOTE - logo
    img = Image.open(logo)
    width, height = img.size
    escala = 0.2
    width = width * escala
    height = height * escala
    cnv.drawImage(logo, x=25, y=730, width=width, height=height)

    #NOTE - Borda
    largura, altura = A4
    cnv.setLineWidth(1.1)
    cnv.roundRect(20, 20, largura-40, altura-40, 10, stroke=1, fill=0)
    cnv.line(x1=20, y1=100, x2=575, y2=100)

    #NOTE - Cabeçalho
    x = 120
    y = 805
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='ESTADO  BAHIA')
    cnv.setFont('font1_bold', 12)
    cnv.drawString(x=x, y=y-15, text='GRANDE ORIENTE DO BRASIL - BAHIA')
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='SECRETARIA DE FINANCAS GOB-BA')
    cnv.setFont('font1_bold', 10)
    cnv.drawString(x=x, y=y-45, text='RUA JOGO DO CARNEIRO, 157 - SAÚDE - 40.045-040')
    cnv.drawString(x=x, y=y-60, text='CNPJ: 14670178000154')
    img = Image.open(qr_code)
    width, height = img.size
    escala = 0.07
    width = width * escala
    height = height * escala
    cnv.drawImage(qr_code, x=495, y=730, width=width, height=height)

    #NOTE - Título
    x = 300
    y = 700
    cnv.setFont('font1_bold', 12)
    cnv.drawCentredString(x=x, y=y, text='CERTIDÃO NEGATIVA DE DÉBITOS')
    cnv.drawCentredString(x=x, y=y-14, text='RELATIVOS ÀS TAXAS DO GRANDE ORIENTE DO BRASIL - BA')

    #NOTE - Dados
    x = 35
    y = 605
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='CNPJ/CPF:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+145, y=y, text=cnpj_cpf)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-15, text='INSCRIÇÃO MUNICIPAL:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+145, y=y-15, text=inscricao_municipal)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='NOME / RAZÃO SOCIAL:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+145, y=y-30, text=razao_social)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-45, text='ENDEREÇO:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+145, y=y-45, text=endereco)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-60, text='MUNICIPIO / UF:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+145, y=y-60, text=municipio_uf)

    #NOTE - Texto
    x = 35
    y = 490
    cnv.setFont('font1', 12)
    cnv.drawString(x=x, y=y, charSpace=0.3, text='Ressalvado o direito da Secretaria de Finanças do Grande Oriente do Brasil – Bahia / GOB-BA')
    cnv.drawString(x=x, y=y-15, charSpace=0.45, text='cobrar e inscrever quaisquer dívidas de responsabilidade da A R L S acima identificada que')
    cnv.drawString(x=x, y=y-30, charSpace=0.3, text='vierem a ser apuradas, é Certificado que não constam pendências em seu nome, relativas as')
    cnv.drawString(x=x, y=y-45, charSpace=0.3, text='taxas administradas.')
    
    #NOTE - Data
    x = 35
    y = 300
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='DATA EMISSÃO:')
    cnv.setFont('font1', 11)
    cnv.drawString(x=x+93, y=y, text=data_emissao)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-15, text='VÁLIDO ATÉ: ')
    cnv.setFont('font1', 11)
    cnv.drawString(x=x+93, y=y-15, text=data_validade)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='CÓDIGO DE VERIFICAÇÃO:')
    cnv.setFont('font1', 11)
    cnv.drawString(x=x+150, y=y-30, text=codigo_verificacao)

    #NOTE - Rodapé
    x = 300
    y = 70
    cnv.setFont('font1_bold', 8)
    cnv.drawCentredString(x=x, y=y, text='E-mail:financeiro.goeb@gmail.com Site: Telefone: (71) 32410420')
    cnv.drawCentredString(x=x, y=y-13, text='Autenticidade do documento sujeita a verificação.')
    cnv.drawCentredString(x=x, y=y-23, text='Acesse: https://gob-ba.link3.com.br/l3-grp/Servicos.html para verificação.')

    cnv.save()

