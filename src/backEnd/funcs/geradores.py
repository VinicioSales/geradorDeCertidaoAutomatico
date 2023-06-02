import os
import qrcode
import datetime
from PIL import Image
from static.img import *
from static.cores import *
from static.fonts import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet


#NOTE - Data
data_atual = datetime.date.today()
data_atual = data_atual.strftime('%d/%m/%Y')
data_atual_2 = datetime.date.today()
data_validade = data_atual_2 + datetime.timedelta(days=30)
data_validade = data_validade.strftime("%d/%m/%Y")

#NOTE - QRCODE
dados = f"Leandro dos Santos Araújo \nEmissão: {data_atual} \nValidade: {data_validade}"
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)
qr.add_data(dados)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(qr_code)

#NOTE - Fontes
pdfmetrics.registerFont(TTFont('font1', font_principal))
pdfmetrics.registerFont(TTFont('font1_bold', font_principal_bold))
styles = getSampleStyleSheet()
style = styles["Normal"]

diretorio_documentos = os.path.join(os.path.expanduser('~'), 'Downloads')

#SECTION - gerar_certidao_positiva
def gerar_certidao_positiva(cnpj_cpf: str, razao_social: str, endereco: str, municipio_uf: str):
    """
    Gera uma certidão positiva de débitos.

    Esta função utiliza as informações fornecidas para gerar um documento PDF contendo a certidão positiva de débitos.

    Parâmetros:
    - cnpj_cpf: str - O número do CNPJ ou CPF do solicitante.
    - razao_social: str - O nome ou razão social do solicitante.
    - endereco: str - O endereço do solicitante.
    - municipio_uf: str - O município e UF (Unidade Federativa) do solicitante.
    """
    cnv = canvas.Canvas(fr'{diretorio_documentos}\CERTIDAO POSITIVA.pdf', pagesize=A4)
    
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
    cnv.drawString(x=x, y=y-15, text='DELEGACIA REGIONAL DO GOB NA BAHIA')
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='SECRETARIA DE FINANCAS GOB-BA')
    cnv.setFont('font1_bold', 10)
    cnv.drawString(x=x, y=y-45, text='Rua da Portas do Carmo, nª 37, Pelourinho')
    cnv.drawString(x=x, y=y-60, text='CNPJ: 32.701.021/0001-20')
    img = Image.open(qr_code)
    width, height = img.size
    escala = 0.25
    width = width * escala
    height = height * escala
    cnv.drawImage(qr_code, x=480, y=720, width=width, height=height)

    #NOTE - Título
    x = 300
    y = 700
    cnv.setFont('font1_bold', 12)
    cnv.drawCentredString(x=x, y=y, text='CERTIDÃO POSITIVA DE DÉBITOS')
    cnv.drawCentredString(x=x, y=y-14, text='RELATIVOS ÀS TAXAS DO GRANDE ORIENTE DO BRASIL - BA')

    #NOTE - Dados
    x = 35
    y = 605
    padding = 160
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='CNPJ/CPF:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y, text=cnpj_cpf)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-15, text='NOME / RAZÃO SOCIAL:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y-15, text=razao_social)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='ENDEREÇO:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y-30, text=endereco)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-45, text='MUNICIPIO / UF:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y-45, text=municipio_uf)

    #NOTE - Texto
    x = 35
    y = 490
    cnv.setFont('font1', 11)
    cnv.drawString(x=x, y=y, charSpace=0.2, text='As informações disponíveis na Secretaria de Finanças do Grande Oriente do Brasil – Bahia /')
    cnv.drawString(x=x, y=y-15, charSpace=0.2, text='GOB-BA, sobre a A∴R∴L∴S∴ acima identificada são insuficientes para a emissão de Certidão')
    cnv.drawString(x=x, y=y-30, charSpace=0.2, text='Negativa ou Positiva Com Efeito Negativo de Débitos.')
    x = 290
    y = 375
    cnv.drawCentredString(x=x, y=y, text='Existem débitos!')
    cnv.drawCentredString(x=x, y=y-15, text='Para consultar sua situação fiscal solicite seu extrato.')

    #NOTE - Rodapé
    x = 300
    y = 70
    cnv.setFont('font1_bold', 8)
    cnv.drawCentredString(x=x, y=y, text='E-mail: financeiro.delegacia@gmail.com')
    cnv.drawCentredString(x=x, y=y-15, text='Telefone: (71) 9 9920-5873')

    cnv.save()
#!SECTION

#SECTION - gerar_certidao_negativa
def gerar_certidao_negativa(cnpj_cpf: str, razao_social: str, endereco: str, municipio_uf: str):
    """
    Gera uma certidão negativa de débitos.

    Esta função utiliza as informações fornecidas para gerar um documento PDF contendo a certidão negativa de débitos.

    Parâmetros:
    - cnpj_cpf: str - O número do CNPJ ou CPF do solicitante.
    - razao_social: str - O nome ou razão social do solicitante.
    - endereco: str - O endereço do solicitante.
    - municipio_uf: str - O município e UF (Unidade Federativa) do solicitante.
    - data_emissao: str - A data de emissão da certidão.
    """
    cnv = canvas.Canvas(fr'{diretorio_documentos}\CERTIDAO NEGATIVA.pdf', pagesize=A4)
    
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
    cnv.drawString(x=x, y=y-15, text='DELEGACIA REGIONAL DO GOB NA BAHIA')
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='SECRETARIA DE FINANCAS GOB-BA')
    cnv.setFont('font1_bold', 10)
    cnv.drawString(x=x, y=y-45, text='Rua da Portas do Carmo, nª 37, Pelourinho')
    cnv.drawString(x=x, y=y-60, text='CNPJ: 32.701.021/0001-20')
    img = Image.open(qr_code)
    width, height = img.size
    escala = 0.25
    width = width * escala
    height = height * escala
    cnv.drawImage(qr_code, x=480, y=720, width=width, height=height)

    #NOTE - Título
    x = 300
    y = 700
    cnv.setFont('font1_bold', 12)
    cnv.drawCentredString(x=x, y=y, text='CERTIDÃO NEGATIVA DE DÉBITOS')
    cnv.drawCentredString(x=x, y=y-14, text='RELATIVOS ÀS TAXAS DO GRANDE ORIENTE DO BRASIL - BA')

    #NOTE - Dados
    x = 35
    y = 605
    padding = 160
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='CNPJ/CPF:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y, text=cnpj_cpf)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-15, text='NOME / RAZÃO SOCIAL:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y-15, text=razao_social)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='ENDEREÇO:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y-30, text=endereco)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-45, text='MUNICIPIO / UF:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y-45, text=municipio_uf)

    #NOTE - Texto
    x = 35
    y = 490
    cnv.setFont('font1', 11)
    cnv.drawString(x=x, y=y, charSpace=0.2, text='Ressalvado o direito da Secretaria de Finanças do Grande Oriente do Brasil – Bahia / GOB-BA')
    cnv.drawString(x=x, y=y-15, charSpace=0.2, text='cobrar e inscrever quaisquer dívidas de responsabilidade da A∴R∴L∴S∴ acima identificada que')
    cnv.drawString(x=x, y=y-30, charSpace=0.2, text='vierem a ser apuradas, é Certificado que não constam pendências em seu nome, relativas as')
    cnv.drawString(x=x, y=y-45, charSpace=0.2, text='taxas administradas.')
    
    #NOTE - Data
    x = 35
    y = 300
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='DATA EMISSÃO:')
    cnv.setFont('font1', 11)
    cnv.drawString(x=x+100, y=y, text=data_atual)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-18, text='VÁLIDO ATÉ: ')
    cnv.setFont('font1', 11)
    cnv.drawString(x=x+100, y=y-15, text=data_validade)
    cnv.setFont('font1_bold', 11)

    #NOTE - Rodapé
    x = 300
    y = 70
    cnv.setFont('font1_bold', 8)
    cnv.drawCentredString(x=x, y=y, text='E-mail: financeiro.delegacia@gmail.com')
    cnv.drawCentredString(x=x, y=y-15, text='Telefone: (71) 9 9920-5873')

    cnv.save()
#!SECTION

#SECTION - gerar_certidao_negativa
def gerar_certidao_positiva_negativa(cnpj_cpf: str, razao_social: str, endereco: str, municipio_uf: str):
    """
    Gera uma certidão positiva com efeito negativo de débitos relativos às taxas do DELEGACIA REGIONAL DO GOB NA BAHIA.

    Parâmetros:
    - cnpj_cpf (str): CNPJ ou CPF do solicitante.
    - razao_social (str): Nome ou razão social do solicitante.
    - endereco (str): Endereço do solicitante.
    - municipio_uf (str): Município e UF do solicitante.
    - data_emissao (str): Data de emissão da certidão.
    """
    cnv = canvas.Canvas(fr'{diretorio_documentos}\CERTIDAO POSITIVA COM EFEITO NEGATIVO.pdf', pagesize=A4)
    
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
    cnv.roundRect(20, 20, largura-40, altura-40, radius=10, stroke=1, fill=0)
    cnv.line(x1=20, y1=100, x2=575, y2=100)

    #NOTE - Cabeçalho
    x = 120
    y = 805
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='ESTADO  BAHIA')
    cnv.setFont('font1_bold', 12)
    cnv.drawString(x=x, y=y-15, text='DELEGACIA REGIONAL DO GOB NA BAHIA')
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='SECRETARIA DE FINANCAS GOB-BA')
    cnv.setFont('font1_bold', 10)
    cnv.drawString(x=x, y=y-45, text='Rua da Portas do Carmo, nª 37, Pelourinho')
    cnv.drawString(x=x, y=y-60, text='CNPJ: 32.701.021/0001-20')
    img = Image.open(qr_code)
    width, height = img.size
    escala = 0.25
    width = width * escala
    height = height * escala
    cnv.drawImage(qr_code, x=480, y=720, width=width, height=height)

    #NOTE - Título
    x = 300
    y = 700
    cnv.setFont('font1_bold', 12)
    cnv.drawCentredString(x=x, y=y, text='CERTIDÃO POSITIVA COM EFEITO NEGATIVO DE DÉBITOS')
    cnv.drawCentredString(x=x, y=y-14, text='RELATIVOS ÀS TAXAS DO GRANDE ORIENTE DO BRASIL - BA')

    #NOTE - Dados
    x = 35
    y = 605
    padding = 160
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='CNPJ/CPF:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y, text=cnpj_cpf)
    cnv.setFillColor(amarelo)
    cnv.roundRect(x=x-3, y=y-19, width=155, height=15, radius=3, stroke = 0, fill=1)
    cnv.setFillColor(preto)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-15, text='NOME / RAZÃO SOCIAL:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y-15, text=razao_social)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='ENDEREÇO:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y-30, text=endereco)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-45, text='MUNICIPIO / UF:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y-45, text=municipio_uf)

    #NOTE - Texto
    x = 35
    y = 490
    cnv.setFont('font1', 11)
    cnv.drawString(x=x, y=y, charSpace=0.2, text='Ressalvado o direito da Secretaria de Finanças do Grande Oriente do Brasil – Bahia / GOB-BA')
    cnv.drawString(x=x, y=y-15, charSpace=0.2, text='cobrar e inscrever quaisquer dívidas de responsabilidade da A∴R∴L∴S∴ acima identificada que')
    cnv.drawString(x=x, y=y-30, charSpace=0.2, text='vierem a ser apuradas, é Certificado que não constam pendências em seu nome, relativas as')
    cnv.drawString(x=x, y=y-45, charSpace=0.2, text='taxas administradas.')
    
    #NOTE - Data
    x = 35
    y = 300
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='DATA EMISSÃO:')
    cnv.setFont('font1', 11)
    cnv.drawString(x=x+100, y=y, text=data_atual)
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-15, text='VÁLIDO ATÉ: ')
    cnv.setFont('font1', 11)
    cnv.drawString(x=x+100, y=y-15, text=data_validade)
    cnv.setFont('font1_bold', 11)

    #NOTE - Rodapé
    x = 300
    y = 70
    cnv.setFont('font1_bold', 8)
    #cnv.setFillColor(amarelo)
    #cnv.roundRect(x=x-160, y=y-3, width=320, height=12, radius=3, stroke = 0, fill=1)
    #cnv.setFillColor(preto)
    cnv.drawCentredString(x=x, y=y, text='E-mail: financeiro.delegacia@gmail.com')
    cnv.drawCentredString(x=x, y=y-15, text='Telefone: (71) 9 9920-5873')

    cnv.save()
#!SECTION
