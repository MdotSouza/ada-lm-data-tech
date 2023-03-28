from projetos.calculadora.funcoes import soma, subtracao, divisao, multiplicacao

def calcule():
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
    a, b = input("Digite o número a: "), input("Digite o número b: ")
    opcao = input(f"Selecione a operaço: {[opcao for opcao in menuFuncoes.keys()]}: ")
    
    if opcao in menuFuncoes:
      print("Resultado: ", menuFuncoes[opcao](a,b))
    else:
      print("Seleção Inválida")