
import os
import qrcode
import datetime
from PIL import Image
from src.backEnd.static.img import *
from src.backEnd.static.cores import *
from src.backEnd.static.fonts import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet

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
    #gerar_qr_code(cnpj_cpf=cnpj_cpf, razao_social=razao_social)
    cnv = canvas.Canvas(fr'C:\Users\Parceiro\Downloads\CERTIDAO POSITIVA - {razao_social}.pdf', pagesize=A4)
    
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
    cnv.drawString(x=x, y=y-45, text='Rua da Portas do carmo, 37 - Pelourinho - 40.026-290')
    cnv.drawString(x=x, y=y-60, text='CNPJ: 32.701.021/0001-20')
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
    cnv.drawCentredString(x=x, y=y-14, text='RELATIVOS ÀS TAXAS DO GRANDE ORIENTE DO BRASIL - BA')

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
    y = 440
    cnv.setFont('font1', 11)
    cnv.drawString(x=x, y=y, charSpace=0.2, text='As informações disponíveis na Secretaria de Finanças da DELEGACIA REGIONAL DO GOB ')
    cnv.drawString(x=x, y=y-15, charSpace=0.2, text='NA BAHIA / GOB-BA, sobre a A∴R∴L∴S∴ acima identificada')
    cnv.drawString(x=x, y=y-30, charSpace=0.2, text='são insuficientes para a emissão de Certidão')
    cnv.drawString(x=x, y=y-45, charSpace=0.2, text='Negativa ou Positiva Com Efeito Negativo de Débitos.')
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

gerar_certidao_positiva('cnpj_cpf', 'razao_social', 'endereco', 'municipio_uf')