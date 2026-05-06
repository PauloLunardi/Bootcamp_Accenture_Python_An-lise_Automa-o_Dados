# Criando um modelo para criação, adição e leitura de conteudo no arquivo em python

# Abrindo o arquivo e escrevendo nele
with open("relatorio.txt", "w") as arquivo:
    arquivo.write("Relatório de vendas\n")
    arquivo.write("Total: 1500")

# Adicionando conteudo no arquivo
with open("telatorio.txt", "a") as arquivo:
    arquivo.write("\nNovo Registro Adicionado.")

# Lendo conteudo no arquivo, linha por linha
with open("telatorio.txt", "r") as arquivo:
    for linha in arquivo:
      print(linha.strip())
