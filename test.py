import shutil
import os

diretorio_downloads = os.path.join(os.path.expanduser('~'), 'Documents')
print(diretorio_downloads)
print(type(diretorio_downloads))

shutil.copy2(r'C:\Users\Parceiro\Meu Drive\Junior\Python\Omie\gerador_de_certidao_GRANDE_ORIENTE_DO_BRASIL\README.md', fr'{diretorio_downloads}\README.md')