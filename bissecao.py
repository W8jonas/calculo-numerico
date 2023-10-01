

def bissecao(f, a, b, tol=1e-2, max_iter=100):
    iteracoes = 0
    
    if (f(a) * f(b) > 0):
        return None, 0

    while iteracoes < max_iter:
        pontoMedio = (a + b) / 2
        
        f_pontoMedio = f(pontoMedio)

        erro_absoluto = abs(b - a)
        erro_relativo = erro_absoluto / abs(b)

        print('| {:10} | {:<20} | {:<25} | {:<25} | {:<25} | {:<25}|'.format(iteracoes, pontoMedio, f(a), f(b), erro_absoluto, erro_relativo))

        if erro_absoluto < tol:
            return pontoMedio, iteracoes
        
        if (f(a) * f_pontoMedio > 0):
            a = pontoMedio
        else:
            b = pontoMedio
        iteracoes += 1
        
    return pontoMedio, iteracoes



def f(x):
    return x**2 - 5


a = 2.0
b = 3.0

print("Método de Bisseção")
print('| {:^10} | {:^20} | {:^25} | {:^25} | {:^25} | {:^25}|'.format("iteracoes", "pontoMedio", "f(a)", "f(b)", "erro_absoluto", "erro_relativo"))

raiz, iteracoes = bissecao(f, a, b)

if raiz is not None:
    print("Convergiu em ", iteracoes, " para ", raiz)
else:
    print("O método não convergiu no intervalo dado após ", iteracoes, "iterações.")
