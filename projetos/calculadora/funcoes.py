def soma(a,b):
    try:
        a, b = int(a), int(b)
        return a + b
    except ValueError as e:
        print(f"O input 'a' e 'b' devem ser um int ou float.")

def subtracao(a,b):
    try:
        a, b = int(a), int(b)
        return a - b
    except ValueError as e:
        print(f"O input 'a' e 'b' devem ser um int ou float.", e)

def divisao(a,b):
    try:
        a, b = int(a), int(b)
        if b != 0:
            return a / b
        else:
            print("Divisão inválida.")
            return 0
    except ValueError as e:
        print(f"O input 'a' e 'b' devem ser um int ou float.", e)


def multiplicacao():
    ...

