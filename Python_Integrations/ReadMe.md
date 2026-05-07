Nota:
      Nesta etapa sera utilizado Google Colab Research
        - É um serviço gratuito do Google que oferece um ambiente de notebooks Jupyter hospedado na nuvem
        - Voltado para programação em Python, ciência de dados e aprendizado de máquina.

Introdução aos arquivos de dados externos

O que são dados externos?
  Em muitos programas, os dados não ficam dentro do próprio código.
  Eles ficam em arquivos externos, como por exemplo:
    - arquivos de texto
    - planilhas
    - bancos de dados
    - APIs na internet

  Usamos Python para:
    - ler os dados
    - processar informações
    - salvar novos resultados

🔄 Diferença entre dump e dumps

      json.dump(obj, arquivo) → grava direto no arquivo.
      json.dumps(obj) → retorna uma string JSON que você pode imprimir ou manipular, mas não salva no arquivo.
      
      resumindo: json.dump pega um objeto Python e escreve no arquivo em formato JSON.
