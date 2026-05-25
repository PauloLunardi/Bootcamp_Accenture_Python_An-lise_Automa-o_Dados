# Antes de refatorar
def processar(lista):
  resultado = []
  for i in lista:
    if i > 10:
      resultado.append(i*2)
    return resultado


# Depois de Fatorar
def processar_numeros(lista):
  return [numero * 2 for numero in lista if numero > 10]
