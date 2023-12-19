

def ler_dados_de_arquivo():
    with open("entrada-pontos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    n = int(linhas[0])
    pontosXY = []

    for i in range(1, n + 1):
        pontos = list(map(float, linhas[i].split()))
        pontosXY.append(pontos)
    
    return n, pontosXY



def calcular_coeficientes_diferenca_dividida(num_pontos, pontos):
    coeficientes = [pontos[i][1] for i in range(num_pontos)]
    for j in range(1, num_pontos):
        for i in range(num_pontos - 1, j - 1, -1):
            coeficientes[i] = (coeficientes[i] - coeficientes[i - 1]) / (pontos[i][0] - pontos[i - j][0])
    return coeficientes


def calcular_interpolar_polinomio_newton(num_pontos, x_interpolacao, pontos):
    coeficientes = calcular_coeficientes_diferenca_dividida(num_pontos, pontos)
    resultado = coeficientes[0]
    produto = 1
    for i in range(1, len(coeficientes)):
        produto *= (x_interpolacao - pontos[i - 1][0])
        resultado += coeficientes[i] * produto
    return resultado



num_pontos, pontos = ler_dados_de_arquivo()

print("Pontos lidos:")
for ponto in pontos:
    print(ponto)

x_interpolacao = float(input("Digite o ponto para interpolação: "))

if x_interpolacao < pontos[0][0] or x_interpolacao > pontos[-1][0]:
    print("O ponto de interpolação está fora do intervalo fornecido.")
else:
    resultado_interpolado = calcular_interpolar_polinomio_newton(num_pontos, x_interpolacao, pontos)
    print(f"O valor interpolado em x = {x_interpolacao} é: {resultado_interpolado}")



