from PIL import Image
from static.variaveis import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet


pdfmetrics.registerFont(TTFont('font1', font_principal))
pdfmetrics.registerFont(TTFont('font1_bold', font_principal_bold))
styles = getSampleStyleSheet()
style = styles["Normal"]

def gerar_certidao_positiva(cnpj_cpf, inscricao_municipal, razao_social, endereco, municipio_uf):
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
    cnv.roundRect(20, 20, largura-40, altura-40, 10, stroke=1, fill=0)

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
    

    cnv.save()


