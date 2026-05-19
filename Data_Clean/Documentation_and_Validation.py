# Documentação e Validação

def validar_dataset(df):

  print("Linhas:", df.shape[0])
  print("Colunas:", df.shape[1])
  print("\nValores Ausentes:")

  print(df.isnull().sum())

# executar após definição de validar_dataset criada acima
# validar_dataset(df) 
