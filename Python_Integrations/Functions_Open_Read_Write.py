# Criando arquivo para teste
with open("dados.txt", "w") as arquivo:
  arquivo.write("Python é uma linguagem de Programação.\n")
  arquivo.write("Aula: Criação de arquivos com Python.\n")

# Lendo o arquivo teste por completo
with open("dados.txt", "r")  as arquivo:
  conteudo = arquivo.read()
print(conteudo)

# Lendo o arquivo teste linha por linha
with open("dados.txt", "r")  as arquivo:
  for linha in arquivo:
    print(linha.strip())

