import logging

logging.basicConfig(level=logging.INFO)

def processar_dados():

  logging.info("Processamento iniciado")
  print(">>> Iniciando execução do cron job...")  # saída direta no console

  vendas = [100, 200, 150]
  total = sum(vendas)

  logging.info("total calculado: %s", total)
  print("Total de vendas:", total)  # saída direta no console

processar_dados()
