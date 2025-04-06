"""
    Program wykorzystujący mechanizm działania Sita Erastotenesa dla zakresu liczb 2 do 100
    Autor: mhSeveeN
"""

def Erastostenes(n):
    A = [True] * (n +1)
    A[0] = A[1] = False
    for i in range(2, int(n**0.5)+1):
        if A[i]:
            for j in range (i*i, n+1, i):
                A[j] = False
    
    return [i for i in range(n+1) if A[i]]

n=100
print(f"Liczby pierwsze mniejsze niż {n}: {Erastostenes(n)}.")