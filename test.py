from datetime import date, datetime
import datetime

dias_uteis = 0
data_atual = datetime.date.today()
dias_a_somar = 10
while dias_uteis < dias_a_somar:
    data_atual += datetime.timedelta(days=1)
    if data_atual.weekday() not in (5, 6):
        dias_uteis += 1
data_vencimento = str(data_atual)
date = datetime.datetime.strptime(data_vencimento, "%Y-%m-%d")
data_vencimento = date.strftime("%d/%m/%Y")

print(data_vencimento)