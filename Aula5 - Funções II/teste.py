def maior_numero(a, b, c):
    maior = a
    
    if b > maior:
        maior = b
    
    if c > maior:
        maior = c
    
    return maior

print(maior_numero(10, 20, 5))    
print(maior_numero(-3, -1, -7))   
print(maior_numero(100, 100, 50)) 
print(maior_numero(7, 7, 7))