def calcular_delta(a, b, c):
    return b**2 - 4*a*c

def calcular_raizes(a, b, c):
    delta = calcular_delta(a, b, c)
    
    if delta < 0:
        return ()  
    
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    
    return (x1, x2)

