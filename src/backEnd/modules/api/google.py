import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_liberacao():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(r'src\backEnd\credenciais_parceiro.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open_by_key('1qdtZic7kKuemciRoDiO25vTfjv7wzQGusw4YA5oqrcI')
    planilha = wks.worksheet('loja_marconica')
    status = planilha.cell(2,1).value

    return status

planilha = get_liberacao()
print(planilha)