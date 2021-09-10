def bhaskara(a, b, c):
    """
    Computa a(s) raíz(es) de um polinômio de segundo grau
    usando a fórmula de bhaskara:

    (-b ± √b² - 4ac) / (2a)
    """
    delta = (b ** 2) - 4 * a * c

    if a == 0:
        print("O valor de a, deve ser diferente de 0")
    elif delta < 0:
        print("Sem raízes reais")
    else:
        x1 = (-b + delta ** (1 / 2)) / (2 * a) 
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        print(f"x1: {x1}, x2: {x2}")
