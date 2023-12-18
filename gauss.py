
def ler_matriz_de_arquivo():
    with open("entrada.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    n = int(linhas[0].strip())  # Número de linhas da matriz
    matriz = []
    
    for linha in linhas[1:]:
        elementos = list(map(float, linha.split()))
        matriz.append(elementos)
    
    return n, matriz


def imprimir_matriz(matriz):
    for linha in matriz:
        print("\t".join(map(str, linha)))


def pivotear_matriz(matriz):
    n = len(matriz)
    
    for k in range(n - 1):
        # Pivoteamento parcial por colunas
        max_element = abs(matriz[k][k])
        max_row = k
        for i in range(k + 1, n):
            if abs(matriz[i][k]) > max_element:
                max_element = abs(matriz[i][k])
                max_row = i
        
        # Faz a troca de posição
        if max_row != k:
            matriz[k], matriz[max_row] = matriz[max_row], matriz[k]
    
    return matriz



def eliminacao_gauss_pivoteamento(matriz):
    n = len(matriz)

    # Eliminação Gauss
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = matriz[i][k] / matriz[k][k]
            for j in range(k, n + 1):
                matriz[i][j] -= factor * matriz[k][j]
    
    # Verifica se a matriz é singular
    for i in range(n):
        if matriz[i][i] == 0:
            return None
    
    # Resolução do sistema por retrosubstituição
    # criando array x com a quantidade de elementos n
    x = [0] * n

    # loop for de n-1 até valor -1, indo de -1 em -1
    for i in range(n - 1, -1, -1):
        x[i] = matriz[i][n] / matriz[i][i]
        for j in range(i - 1, -1, -1):
            matriz[j][n] -= matriz[j][i] * x[i]
    
    return x




n, matriz = ler_matriz_de_arquivo()

print("Matriz original:")
imprimir_matriz(matriz)

# Duplicando a matriz / para cada linha row, preencher com o valor de cada linha da matriz
matriz_pivoteada = [row[:] for row in matriz]
matriz_pivoteada = pivotear_matriz(matriz_pivoteada)

matriz_escalada = [row[:] for row in matriz]
solucao = eliminacao_gauss_pivoteamento(matriz_escalada)


if solucao:
    print("\nMatriz pivoteada:")
    imprimir_matriz(matriz_pivoteada)
    
    print("\nMatriz escalonada:")
    imprimir_matriz(matriz_escalada)
    
    print("\nVetor de solução:", solucao)
else:
    print("\nA matriz é singular. Não há solução.")
