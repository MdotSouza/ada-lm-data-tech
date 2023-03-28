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

def divisao():
    ...

def multiplicacao():
    ...

