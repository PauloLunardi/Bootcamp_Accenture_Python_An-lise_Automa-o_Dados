# essa função seria o que o Cron Jobs rodaria, chando o arquivo.py 
# gerando  "log" com a hora que foi chamado e o total das vendas
import datetime

def generate_report():

  sales = [120, 200, 150,300]

  total = sum(sales)

  now = datetime.datetime.now()

  print("Report generated in:", now)
  print("Sales total:", total)

generate_report()
