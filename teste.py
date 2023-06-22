from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet

pdfmetrics.registerFont(TTFont('font1_bold', r'src\backEnd\fonts\DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('font1', r'src\backEnd\fonts\DejaVuSans.ttf'))

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
    #gerar_qr_code(cnpj_cpf=cnpj_cpf, razao_social=razao_social)
    cnv = canvas.Canvas(fr'CERTIDAO POSITIVA COM EFEITO NEGATIVO - {razao_social}.pdf', pagesize=A4)
    
    #NOTE - logo
    #img = Image.open(logo)
    #width, height = img.size
    escala = 0.2
    # width = width * escala
    # height = height * escala
    #LINK - cnv.drawImage(logo, x=25, y=730, width=width, height=height)

    #NOTE - Borda
    largura, altura = A4
    cnv.setLineWidth(1.1)
    cnv.roundRect(20, 20, largura-40, altura-40, radius=10, stroke=1, fill=0)
    cnv.line(x1=20, y1=100, x2=575, y2=100)

    #NOTE - Cabeçalho
    x = 120
    y = 805
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='GRANDE ORIENTE DO BRASIL - BAIANO')
    cnv.setFont('font1_bold', 12)
    cnv.drawString(x=x, y=y-15, text='SECRETARIA DE FINANCAS GOB-BAIANO')
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y-30, text='Rua da Portas do carmo, 37 - Pelourinho - 40.026-290')
    cnv.setFont('font1_bold', 10)
    cnv.drawString(x=x, y=y-45, text='CNPJ: 51.130.499/0001-92')
    #img = Image.open(qr_code)
    #width, height = img.size
    escala = 0.2
    # width = width * escala
    # height = height * escala
    #cnv.drawImage(qr_code, x=460, y=700, width=width, height=height)

    #NOTE - Título
    x = 300
    y = 650
    cnv.setFont('font1_bold', 12)
    cnv.drawCentredString(x=x, y=y, text='CERTIDÃO POSITIVA COM EFEITO NEGATIVO DE DÉBITOS')
    cnv.drawCentredString(x=x, y=y-14, text='RELATIVOS ÀS TAXAS DO GRANDE ORIENTE DO BRASIL - BAIANO')

    #NOTE - Dados
    x = 35
    y = 555
    padding = 160
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='CNPJ/CPF:')
    cnv.setFont('font1', 10)
    cnv.drawString(x=x+padding, y=y, text=cnpj_cpf)
    # cnv.setFillColor(amarelo)
    # cnv.roundRect(x=x-3, y=y-19, width=155, height=15, radius=3, stroke = 0, fill=1)
    # cnv.setFillColor(preto)
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
    cnv.drawString(x=x, y=y, charSpace=0.2, text='Ressalvado o direito da Secretaria de Finanças da GRANDE ORIENTE DO BRASIL - BAIANO')
    cnv.drawString(x=x, y=y-15, charSpace=0.2, text='cobrar e inscrever quaisquer dívidas de responsabilidade da A∴R∴L∴S∴ acima')
    cnv.drawString(x=x, y=y-30, charSpace=0.2, text='identificada que vierem a ser apuradas, é Certificado que não constam pendências')
    cnv.drawString(x=x, y=y-45, charSpace=0.2, text='em seu nome, relativas as taxas administradas.')
    
    #NOTE - Data
    x = 35
    y = 300
    cnv.setFont('font1_bold', 11)
    cnv.drawString(x=x, y=y, text='DATA EMISSÃO:')
    # cnv.setFont('font1', 11)
    # cnv.drawString(x=x+100, y=y, text=data_atual)
    # cnv.setFont('font1_bold', 11)
    # cnv.drawString(x=x, y=y-15, text='VÁLIDO ATÉ: ')
    # cnv.setFont('font1', 11)
    # cnv.drawString(x=x+100, y=y-15, text=data_validade)
    # cnv.setFont('font1_bold', 11)

    #NOTE - Rodapé
    x = 300
    y = 70
    cnv.setFont('font1_bold', 8)
    cnv.drawCentredString(x=x, y=y, text='E-mail: financeiro.delegacia@gmail.com')
    cnv.drawCentredString(x=x, y=y-15, text='Telefone: (71) 9 9920-5873')

    cnv.save()

gerar_certidao_positiva_negativa('123', '123', '123', '21')
