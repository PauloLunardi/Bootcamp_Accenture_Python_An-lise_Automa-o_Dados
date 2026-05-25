# Versão não otimizada

def processar(lista):

    lista_filtrada = []

    for x in lista:

        if x > 10:
            lista_filtrada.append(x)

    resultado = []

    for numero in lista_filtrada:

        resultado.append(numero * 2)

    return resultado


# Versão Otimizada do código complexo

def processar(lista):
  return [x*2 for x in lista if x > 10]
