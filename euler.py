def e_cuadratica(n):
    # Implemente esta función
    if n == 0:
    	return 1
    if n == 1:
    	return n 
    return (1/factorial(n) + e_cuadratica(n-1))


def e_lineal(n):
    # Implemente esta función
    i = 0
    a = 1
    while i < n:
   		a = a + 1/factorial(i)
    return a
