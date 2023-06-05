import gspread
from oauth2client.service_account import ServiceAccountCredentials

#NOTE - get_liberacao
def get_liberacao():
    """
    Obtém o status de liberação de acordo com a planilha do Google.

    Returns:
        str: O status de liberação.
    """
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(r'src\backEnd\credenciais_parceiro.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open_by_key('1qdtZic7kKuemciRoDiO25vTfjv7wzQGusw4YA5oqrcI')
    planilha = wks.worksheet('gerador_de_certidao_GRANDE_ORIENTE_DO_BRASIL')
    status = planilha.cell(2,1).value

    return status
