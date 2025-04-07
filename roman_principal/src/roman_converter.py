def decimal_to_roman(n):
    if not (1 <= n <= 3999):
        raise ValueError("El número debe estar entre 1 y 3999")

    valores = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]

    simbolos = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    resultado = ""
    i = 0

    while n > 0:
        while n >= valores[i]:
            resultado += simbolos[i]
            n -= valores[i]
        i += 1

    return resultado
