from projetos.calculadora.funcoes import soma, subtracao, divisao, multiplicacao

def calcule():
    #montagem do menu de funções
    menuFuncoes = {
        'soma':soma,
        'subtracao':subtracao,
        'divisao':divisao,
        'multiplicacao':multiplicacao,
        '+': soma,
        '-':subtracao,
        '*':multiplicacao,
        '/':divisao
    }
    
    #####solicitação e tratamento das entradas de números#####
    a, b = input("Digite o número a: ").replace(",","."), input("Digite o número b: ").replace(",",".")

    #verifica se foram digitadas letras
    caracteres = '0123456789.'
    if not set(a).intersection(caracteres) or not set(b).intersection(caracteres):
       raise ValueError("Não é possível convertar as entradas.")
    a,b = float(a),float(b)

    #solicitação e tratamento da entrada de opção
    opcao = input(f"Selecione a operaço: {[opcao for opcao in menuFuncoes.keys()]}: ")

    if opcao in menuFuncoes:
      print("Resultado: ", menuFuncoes[opcao](a,b))
    else:
      raise RuntimeError("Seleção Inválida")