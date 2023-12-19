

def ler_dados_de_arquivo():
    with open("entrada-pontos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    n = int(linhas[0])  # Número de linhas da matriz
    pontosXY = []

    for i in range(1, n + 1):
        pontos = list(map(float, linhas[i].split()))
        pontosXY.append(pontos)
    
    return n, pontosXY


def imprimir_array(array):
    print("\n")
    for linha in array:
        print("\t".join(map(str, linha)))
    print("\n")


def imprimir_resultado(coeficientes, tipo="linear"):
    print("\n")
    print("Coeficientes:", coeficientes)
    print("Função:")
    if (tipo == "linear"):
        print(f"{coeficientes[0]}x + {coeficientes[1]}")

    if (tipo == "quadratica"):
        print(f"{coeficientes[2]}x² + {coeficientes[1]}x + {coeficientes[0]}")

    print("\n")
    print(f"Raiz da média quadrática dos resíduos (RMSE): {rmse} \n\n\n")



def resolve_sistema_gauss_seidel(matriz, b, x0, epsilon=1e-5, max_iter=100):

    n = len(matriz)
    x = x0.copy()
    
    iteracoes = 0
    while iteracoes < max_iter:
        iteracoes += 1
        x_antigo = x.copy()

        for lin in range(n):
            soma = 0
            for col in range(n):
                if col != lin:
                    soma += matriz[lin][col] * x[col] / matriz[lin][lin]
                    
                x[lin] = (b[lin] / matriz[lin][lin]) - soma

        # Cálculo da diferença relativa em norma infinito
        diff_rel = max(abs(x[i] - x_antigo[i]) / abs(x[i]) for i in range(n))
        
        if diff_rel < epsilon or iteracoes == max_iter:
            return [round(xi, 3) for xi in x]
        
    return None  # Falha




def minimos_quadrados_linear(num_pontos, pontos):
    x = [ponto[0] for ponto in pontos]
    y = [ponto[1] for ponto in pontos]

    somatorio_x = sum(x)
    somatorio_y = sum(y)
    somatorio_x2 = sum(xi**2 for xi in x)

    somatorio_xy = 0
    for xy in pontos:
        somatorio_xy += xy[0] * xy[1]


    # Calcula os coeficientes a0 e a1
    a1 = (num_pontos * somatorio_xy - somatorio_x * somatorio_y) / (num_pontos * somatorio_x2 - somatorio_x**2)
    a0 = (somatorio_y - a1 * somatorio_x) / num_pontos

    # Calcula os valores preditos y_pred
    y_pred = [a0 + a1 * xi for xi in x]

    # Calcula os resíduos
    residuos = [yi - y_predi for yi, y_predi in zip(y, y_pred)]

    # Calcula a raiz da média quadrática dos resíduos
    rmse = (sum(residual**2 for residual in residuos) / num_pontos)**0.5

    return a0, a1, rmse


def calcular_regressao_quadratica(num_pontos, pontos):
    x = [ponto[0] for ponto in pontos]
    y = [ponto[1] for ponto in pontos]

    somatorio_x = sum(x)
    somatorio_y = sum(y)
    somatorio_x2 = sum(xi**2 for xi in x)
    somatorio_x3 = sum(xi**3 for xi in x)
    somatorio_x4 = sum(xi**4 for xi in x)
    
    somatorio_xy = 0
    for ponto in pontos:
        somatorio_xy += ponto[0] * ponto[1]

    somatorio_x2y = 0
    for ponto in pontos:
        somatorio_x2y += ponto[0] * ponto[0] * ponto[1]


    # Resolve o sistema linear
    coeficientes = resolve_sistema_gauss_seidel(
        [
            [num_pontos, somatorio_x, somatorio_x2],
            [somatorio_x, somatorio_x2, somatorio_x3],
            [somatorio_x2, somatorio_x3, somatorio_x4],
        ],
        [somatorio_y, somatorio_xy, somatorio_x2y],
        [0, 0, 0]
    )
    

    # Calcula os valores preditos y_pred
    y_pred = [coeficientes[0] + coeficientes[1] * xi + coeficientes[2] * xi**2 for xi in x]

    # Calcula os resíduos
    residuos = []
    for i in range(0, 3):
        residuos.append(y[i] - y_pred[i])

    # Calcula a raiz da média quadrática dos resíduos
    rmse = (sum(residual**2 for residual in residuos) / num_pontos)**0.5

    return coeficientes, rmse



def minimos_quadrados_expo(num_pontos, pontos):
    x = [ponto[0] for ponto in pontos]
    y = [ponto[1] for ponto in pontos]

    somatorio_x = sum(x)
    somatorio_y = sum(y)
    somatorio_x2 = sum(xi**2 for xi in x)

    somatorio_xy = 0
    for xy in pontos:
        somatorio_xy += xy[0] * xy[1]


    # Calcula os coeficientes a0 e a1
    a1 = (num_pontos * somatorio_xy - somatorio_x * somatorio_y) / (num_pontos * somatorio_x2 - somatorio_x**2)
    a0 = (somatorio_y - a1 * somatorio_x) / num_pontos

    # Calcula os valores preditos y_pred
    y_pred = [a0 + a1 * xi for xi in x]

    # Calcula os resíduos
    residuos = [yi - y_predi for yi, y_predi in zip(y, y_pred)]

    # Calcula a raiz da média quadrática dos resíduos
    rmse = (sum(residual**2 for residual in residuos) / num_pontos)**0.5

    return a0, a1, rmse




n, pontosXY = ler_dados_de_arquivo()

print("Pontos lidos:")
imprimir_array(pontosXY)


a0, a1, rmse = minimos_quadrados_linear(n, pontosXY)
imprimir_resultado([a0, a1], rmse)


coeficientes, rmse = calcular_regressao_quadratica(n, pontosXY)
imprimir_resultado(coeficientes, rmse, "quadratica")


coeficientes, rmse = minimos_quadrados_expo(n, pontosXY)
imprimir_resultado(coeficientes, rmse, "expo")

