def e_cuadratica(n):
    # Implemente esta función
    if n == 0:
    	return 1
    if n == 1:
    	return n 
    return (1/factorial(n) + e_cuadratica(n-1))


def e_lineal(n):
    # Implemente esta función
    for i in n:
   		a = sum(1/factorial(i))
    return a
