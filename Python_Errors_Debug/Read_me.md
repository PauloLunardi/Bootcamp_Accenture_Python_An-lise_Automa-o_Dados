# O que são erros?

Durante a execução de um programa podem ocorrer erros inesperados.

    Esses erros são chamdos de excessões.
    Eles acontece quando o Python encontra uma situação que não consegue executar.
    Exemplos:
        - Dividir um número por zero.
        - Acessar um arquivo que não existe.
        - Converter texto para um número de forma incorreta
        
  ### Exemplo de erro divisão por zero:
    numero = 10/0
    print(numero)

## Tipos de erros em Python

    Alguns erros comuns são:
      Tipo de erro:       Descrição:
        SyntaxError        erro de sintaxe
        TypeError          operação com tipo incorreto
        ValueError         valor inválido
        ZeroDivisorError   divisão por zero
        FileNotFoundError  arquivo nao encontrado

  ### Exemplo de ValueError:
    numero = int("abc")

## Try / Except

  O bloco try permite tentar executar um código.
    - Se ocorrer um erro, o except captura esse erro.
    
  ### Exemplo:
      try:
        numero = 10/0
        print(numero)
      except ZeroDivisionError:
          print('Erro: divisão por zero')

## Bloco finally

  O bloco finally executa independentemente de ocorrer erro ou não.
    - Se ocorrer um erro, o except captura esse erro se não ocorrer ele finaliza.

  ### Exemplo:
      try:
        numero = int("10")
        print(numero)
      except ValueError:
          print('Erro de conversão')
      finally:  
        print('Execução finalizada')

## Usando raise

  A palavra raise permite gerar um erro manualmente

  ### Exemplo:
      idade = -5

      if idade < 0:
      raise ValueError('Idade não pode ser negativa')

## Depuração (Debugging)

  Depurar significa encontrar e corrigir erros no código.

    Print Debugging:
      - Uma forma simples de depurar é usar print() para verificar valores

  ### Exemplo:
      numero = 10
      divisor = 0

      print('numero:', numero)
      print('divisor:', divisor)

      resultado = numero / divisor

## Stack Trace

  Quando ocorre um erro, o Python mostra um stack trace.

    Ele indica:
      - Onde ocorreu o erro.
      - Qual linha casou o problema.

  ### Exemplo:
        def dividir(a,b):
          return a/b

        dividir(10,0)

# Logs e Monitoramento

Em sistemas reais usamos logs para registrar eventos do sistema.

## Módulo logging:
      - Python possui um módulo chamado logging para registrar informações importantes.
        
  ### Exemplo de erro divisão por zero:
    import logging

    logging.basicConfig(level=logging.INFO)
    logging.info('Programa Iniciado')

## Níveis de log:
      - Existem diferentes níveis de logs.
      Nivel:      Uso:
      DEBUG        Informações detalhadas
      INFO         Informações gerais
      WARNING      Possiveis problemas
      ERROR        Erro ocorrido
      CRITICAL     Erro grave

  ### Exemplo:

    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Menagem de debug')
    logging.info('Mensagem de warning')
    logging.error('Mensagem de erro')

## Monitoramento de scripts
    
 ### Logs ajudam a:
    - Identificar erros
    - Entender o funcionamento do sistema
    - Monitorar scripts automatizados

## Boas Práticas

## Prevenção de erros
    Sempre que possivel devemos prevenir erros antes que aconteçam.
