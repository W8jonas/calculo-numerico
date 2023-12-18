
def ler_matriz_de_arquivo():
    with open("entrada.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    n = int(linhas[0].strip())
    matriz = []
    
    for linha in linhas[1:]:
        elementos = list(map(float, linha.split()))
        matriz.append(elementos)
    
    return n, matriz


def imprimir_matriz(matriz):
    for linha in matriz:
        print("\t".join(map(str, linha)))



def gauss_seidel(matriz, b, x0, epsilon=1e-5, max_iter=10):
    n = len(matriz)
    x = x0.copy()
    
    iteracoes = 0
    while iteracoes < max_iter:
        iteracoes += 1
        x_antigo = x.copy()
        
        for i in range(n):
            soma = sum(matriz[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - soma) / matriz[i][i]
        
        # Cálculo da diferença relativa em norma infinito
        diff_rel = max(abs(x[i] - x_antigo[i]) / max(abs(x[i]), 1e-10) for i in range(n))
        
        if diff_rel < epsilon:
            return x
        
    return None  # Falha


def jacobi(matriz, b, x0, epsilon=1e-5, max_iter=10):
    n = len(matriz)
    x = x0.copy()
    
    iteracoes = 0
    while iteracoes < max_iter:
        iteracoes += 1
        x_antigo = x.copy()
        for i in range(n):
            # soma = sum(matriz[i][j] * (x_antigo[j]/matriz[i][i]) for j in range(n))
            # x[i] = (b[i] / matriz[i][i]) - soma
            
            soma = sum( matriz[i][j] * x_antigo[j] for j in range(n) if j != i )
            x[i] = (b[i] - soma) / matriz[i][i]
        
        # Cálculo da diferença relativa em norma infinito
        diff_rel = max(abs(x[i] - x_antigo[i]) / max(abs(x[i]), 1e-10) for i in range(n))
        
        print(x_antigo, diff_rel)
        if diff_rel < epsilon:
            return x
        
    return None  # Falha




n, matriz = ler_matriz_de_arquivo()

print("Matriz original:")
imprimir_matriz(matriz)

# Separa a matriz dos termos independentes
A = [[matriz[i][j] for j in range(n)] for i in range(n)]
b = [matriz[i][n] for i in range(n)]

# Define o vetor inicial (substitua com sua própria inicialização)
x0 = [0] * n

print("\nMatriz condicionada:")
imprimir_matriz(A)

print("\nVetor inicial:")
print(x0)

# Resolve pelo método de Gauss-Seidel
solucao_gauss_seidel = gauss_seidel(A, b, x0)

if solucao_gauss_seidel:
    print("\nSolução pelo método de Gauss-Seidel:")
    print(solucao_gauss_seidel)
else:
    print("\nFalha ao encontrar a solução pelo método de Gauss-Seidel.")

# Resolve pelo método de Jacobi
solucao_jacobi = jacobi(A, b, x0)

if solucao_jacobi:
    print("\nSolução pelo método de Jacobi:")
    print(solucao_jacobi)
else:
    print("\nFalha ao encontrar a solução pelo método de Jacobi.")
