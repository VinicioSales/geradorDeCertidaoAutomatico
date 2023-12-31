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
def gerar_qr_code(cnpj_cpf, razao_social, data_validade: str):
    data_hora_atual = datetime.datetime.now()
    data_hora_formatada = data_hora_atual.strftime('%d/%m/%Y %H:%M:%S')
    dados = f"Leandro dos Santos Araújo \nEmissão: {data_atual} \nValidade: {data_validade}"
    dados = f"""
    CNPJ/CPF = {cnpj_cpf}
    Nome = {razao_social}


    Data Emissão = {data_atual}
    Válida até = {data_validade}

    Emitida por = LEANDRO DOS SANTOS ARAUJO EM {data_hora_formatada}"""
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
    gerar_qr_code(cnpj_cpf=cnpj_cpf, razao_social=razao_social, data_validade=data_validade)
    cnv = canvas.Canvas(fr'{diretorio_documentos}\CERTIDAO POSITIVA - {razao_social}.pdf', pagesize=A4)
    
    #NOTE - logo
    img = Image.open(logo)
    width, height = img.size
    escala = 0.05
    width = width * escala
    height = height * escala
    cnv.drawImage(logo, x=30, y=735, width=width, height=height)

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
    cnv.drawString(x=x, y=y-15, text='NOME DA EMPRESA')
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='SUBTITULO DA EMPRESA')
    cnv.setFont('font1_bold', 10)
    cnv.drawString(x=x, y=y-45, text='ENDEREÇO')
    cnv.drawString(x=x, y=y-60, text='CNPJ DA EMPRESA')
    img = Image.open(qr_code)
    width, height = img.size
    escala = 0.2
    width = width * escala
    height = height * escala
    cnv.drawImage(qr_code, x=460, y=700, width=width, height=height)

    #NOTE - Título
    x = 300
    y = 650
    cnv.setFont('font1_bold', 12)
    cnv.drawCentredString(x=x, y=y, text='CERTIDÃO POSITIVA DE DÉBITOS')
    cnv.drawCentredString(x=x, y=y-14, text='RELATIVOS ÀS TAXAS DO NOME DA EMPRESA')

    #NOTE - Dados
    x = 35
    y = 555
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
    y = 410
    cnv.setFont('font1', 11)
    cnv.drawString(x=x, y=y, charSpace=0.2, text='As informações disponíveis na nome da empresa,')
    cnv.drawString(x=x, y=y-15, charSpace=0.2, text='sobre a nome do orgão acima identificada são insuficientes para a emissão de Certidão Negativa')
    cnv.drawString(x=x, y=y-30, charSpace=0.2, text='ou Positiva Com Efeito Negativo de Débitos.')
    x = 290
    y = 325
    cnv.drawCentredString(x=x, y=y, text='Existem débitos!')
    cnv.drawCentredString(x=x, y=y-15, text='Para consultar sua situação fiscal solicite seu extrato.')

    #NOTE - Rodapé
    x = 300
    y = 70
    cnv.setFont('font1_bold', 8)
    cnv.drawCentredString(x=x, y=y, text='E-mail')
    cnv.drawCentredString(x=x, y=y-15, text='Telefone')

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
    gerar_qr_code(cnpj_cpf=cnpj_cpf, razao_social=razao_social, data_validade=data_validade)
    cnv = canvas.Canvas(fr'{diretorio_documentos}\CERTIDAO NEGATIVA - {razao_social}.pdf', pagesize=A4)
    
    #NOTE - logo
    img = Image.open(logo)
    width, height = img.size
    escala = 0.05
    width = width * escala
    height = height * escala
    cnv.drawImage(logo, x=30, y=735, width=width, height=height)

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
    cnv.drawString(x=x, y=y-15, text='NOME DA EMPRESA')
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='SUBTITULO DA EMPRESA')
    cnv.setFont('font1_bold', 10)
    cnv.drawString(x=x, y=y-45, text='ENDEREÇO')
    cnv.drawString(x=x, y=y-60, text='CNPJ DA EMPRESA')
    img = Image.open(qr_code)
    width, height = img.size
    escala = 0.2
    width = width * escala
    height = height * escala
    cnv.drawImage(qr_code, x=460, y=700, width=width, height=height)

    #NOTE - Título
    x = 300
    y = 650
    cnv.setFont('font1_bold', 12)
    cnv.drawCentredString(x=x, y=y, text='CERTIDÃO NEGATIVA DE DÉBITOS')
    cnv.drawCentredString(x=x, y=y-14, text='RELATIVOS ÀS TAXAS DO NOME DA EMPRESA')

    #NOTE - Dados
    x = 35
    y = 555
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
    y = 410
    cnv.setFont('font1', 11)
    cnv.drawString(x=x, y=y, charSpace=0.2, text='Ressalvado o direito da nome da empresa')
    cnv.drawString(x=x, y=y-15, charSpace=0.2, text='cobrar e inscrever quaisquer dívidas de responsabilidade da nome do orgão acima')
    cnv.drawString(x=x, y=y-30, charSpace=0.2, text='identificada que vierem a ser apuradas, é Certificado que não constam pendências')
    cnv.drawString(x=x, y=y-45, charSpace=0.2, text='em seu nome, relativas as taxas administradas.')
    
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
    cnv.drawCentredString(x=x, y=y, text='E-mail')
    cnv.drawCentredString(x=x, y=y-15, text='Telefone')

    cnv.save()
#!SECTION

#SECTION - gerar_certidao_positiva_negativa
def gerar_certidao_positiva_negativa(cnpj_cpf: str, razao_social: str, endereco: str, municipio_uf: str, data_vencimento: str):
    """
    Gera uma certidão positiva com efeito negativo de débitos relativos às taxas do DELEGACIA REGIONAL DO GOB NA BAHIA.

    Parâmetros:
    - cnpj_cpf (str): CNPJ ou CPF do solicitante.
    - razao_social (str): Nome ou razão social do solicitante.
    - endereco (str): Endereço do solicitante.
    - municipio_uf (str): Município e UF do solicitante.
    - data_emissao (str): Data de emissão da certidão.
    """
    gerar_qr_code(cnpj_cpf=cnpj_cpf, razao_social=razao_social, data_validade=data_vencimento)
    cnv = canvas.Canvas(fr'{diretorio_documentos}\CERTIDAO POSITIVA COM EFEITO NEGATIVO - {razao_social}.pdf', pagesize=A4)
    
    #NOTE - logo
    img = Image.open(logo)
    width, height = img.size
    escala = 0.05
    width = width * escala
    height = height * escala
    cnv.drawImage(logo, x=30, y=735, width=width, height=height)

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
    cnv.drawString(x=x, y=y-15, text='NOME DA EMPRESA')
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='SUBTITULO DA EMPRESA')
    cnv.setFont('font1_bold', 10)
    cnv.drawString(x=x, y=y-45, text='ENDEREÇO')
    cnv.drawString(x=x, y=y-60, text='CNPJ DA EMPRESA')
    img = Image.open(qr_code)
    width, height = img.size
    escala = 0.2
    width = width * escala
    height = height * escala
    cnv.drawImage(qr_code, x=460, y=700, width=width, height=height)

    #NOTE - Título
    x = 300
    y = 650
    cnv.setFont('font1_bold', 12)
    cnv.drawCentredString(x=x, y=y, text='CERTIDÃO POSITIVA COM EFEITO NEGATIVO DE DÉBITOS')
    cnv.drawCentredString(x=x, y=y-14, text='RELATIVOS ÀS TAXAS DO NOME DA EMPRESA')

    #NOTE - Dados
    x = 35
    y = 555
    padding = 160
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='CNPJ/CPF:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y, text=cnpj_cpf)
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
    y = 410
    cnv.setFont('font1', 11)
    cnv.drawString(x=x, y=y, charSpace=0.2, text='Ressalvado o direito da nome da empresa')
    cnv.drawString(x=x, y=y-15, charSpace=0.2, text='cobrar e inscrever quaisquer dívidas de responsabilidade da nome do orgão acima')
    cnv.drawString(x=x, y=y-30, charSpace=0.2, text='identificada que vierem a ser apuradas, é Certificado que não constam pendências')
    cnv.drawString(x=x, y=y-45, charSpace=0.2, text='em seu nome, relativas as taxas administradas.')
    
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
    cnv.drawString(x=x+100, y=y-15, text=data_vencimento)
    cnv.setFont('font1_bold', 11)

    #NOTE - Rodapé
    x = 300
    y = 70
    cnv.setFont('font1_bold', 8)
    cnv.drawCentredString(x=x, y=y, text='E-mail')
    cnv.drawCentredString(x=x, y=y-15, text='Telefone')

    cnv.save()
#!SECTION
