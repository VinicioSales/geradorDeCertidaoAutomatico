from PIL import Image
from static.variaveis import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.ttfonts import TTFont


pdfmetrics.registerFont(TTFont('arialth', font_principal))


def gerar_certidao_positiva():
    cnv = canvas.Canvas('CERTIDAO POSITIVA.pdf', pagesize=A4)
    largura, altura = A4
    cnv.roundRect(20, 20, largura-40, altura-40, 5, stroke=1, fill=0)
    cnv.setFont('arialth', 11)
    img = Image.open(logo)
    width, height = img.size
    escala = 0.5
    width = width * escala
    height = height * escala
    cnv.drawImage(logo, x=100, y=100, width=width, height=height)


    cnv.save()


