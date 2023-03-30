def soma(a,b):
    if isinstance(a,(int,float)) and isinstance(a,(int,float)):
        return a + b
    raise TypeError(f"O input 'a' e 'b' não devem ser uma string. Recebido {a}, tipo {type(a)}, {b} tipo {type(b)}")

def subtracao(a,b):
    if isinstance(a,(int,float)) and isinstance(a,(int,float)):
        return a - b
    raise TypeError(f"O input 'a' e 'b' não devem ser uma string. Recebido {a}, tipo {type(a)}, {b} tipo {type(b)}")

def divisao(a,b):
    
    if isinstance(a,(int,float)) and isinstance(a,(int,float)):
        if b != 0:
            return a / b
        raise ZeroDivisionError("A divisão por ZERO é inválida.")
    raise TypeError(f"O input 'a' e 'b' não devem ser uma string. Recebido {a}, tipo {type(a)}, {b} tipo {type(b)}")

def multiplicacao(a,b):
    if isinstance(a,(int,float)) and isinstance(a,(int,float)):
        return a * b
    raise TypeError(f"O input 'a' e 'b' não devem ser uma string. Recebido {a}, tipo {type(a)}, {b} tipo {type(b)}")
