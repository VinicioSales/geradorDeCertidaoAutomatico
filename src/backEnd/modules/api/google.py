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
    wks = gc.open_by_key('1ZM4SIz5AEnPoyTBjF6mlm5nx6_e3fmjpNEaj9OE57qc')
    planilha = wks.worksheet('Página1')
    status = planilha.cell(2,2).value
    print(status)
    return status
