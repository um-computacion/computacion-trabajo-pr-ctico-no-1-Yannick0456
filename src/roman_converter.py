def decimal_to_roman(number):
    if number < 1 or number > 3999:
        raise ValueError("El número debe estar entre 1 y 3999")
    
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]



    roman = ""
    i = 0
    while number > 0:
        for _ in range(number // val[i]):
            roman += syms[i]
            number -= val[i]
        i += 1
    return roman

