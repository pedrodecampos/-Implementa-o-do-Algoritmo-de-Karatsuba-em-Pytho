def karatsuba(x, y):
    # Caso base: se os números tiverem 1 dígito, multiplica diretamente
    if x < 10 or y < 10:
        return x * y
    
    # Calcula o número de dígitos do menor número
    n = min(len(str(x)), len(str(y)))
    m = n // 2
    
    # Divide os números em duas partes
    potencia = 10 ** m
    a = x // potencia
    b = x % potencia
    c = y // potencia
    d = y % potencia
    
    # Calcula os três produtos necessários
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd
    
    # Combina os resultados
    return ac * 10**(2*m) + ad_bc * 10**m + bd

# Exemplo de uso
if __name__ == "__main__":
    num1 = 1234
    num2 = 5678
    resultado = karatsuba(num1, num2)
    print(f"Multiplicação de {num1} x {num2} = {resultado}") 
