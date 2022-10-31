def soma(a, b):
    """
    args:
        a: (int, float)
        b: (int, float)
    return:
        a + b -> (int, float)
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser um número, recebido {a} ({type(a)}), b ({type(b)})")


def subtracao(a, b):
    """
    args:
        a: (int, float)
        b: (int, float)
    return:
        a - b -> (int, float)
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser um número, recebido {a} ({type(a)}), b ({type(b)})")


def divisao(a, b):
    """
    args:
        a: (int, float)
        b: (int, float)
    return:
        a / b -> (int, float)
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if b == 0:
            print('Divisão invalida, recebido 0 como denominador')
            return 0
        else:
            return a / b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser um número, recebido {a} ({type(a)}), b ({type(b)})")


def multiplicacao(a, b):
    """
    args:
        a: (int, float)
        b: (int, float)
    return:
        a * b -> (int, float)
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser um número, recebido {a} ({type(a)}), b ({type(b)})")