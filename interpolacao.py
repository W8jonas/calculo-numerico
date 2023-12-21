

def ler_dados_de_arquivo():
    with open("entrada-pontos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    n = int(linhas[0])
    pontosXY = []

    for i in range(1, n + 1):
        pontos = list(map(float, linhas[i].split()))
        pontosXY.append(pontos)
    
    return n, pontosXY


def calcula_por_lagrange(nn, pontos, pontoACalcular):
    yp = 0
    for k in range(0, nn):
        p = 1
        for j in range(0, nn):
            if (k != j):
                p = p * (pontoACalcular - pontos[j][0]) / (pontos[k][0] - pontos[j][0])
        yp = yp + p * pontos[k][1]

    return yp


num_pontos, pontos = ler_dados_de_arquivo()

print("\nPontos lidos:")
for ponto in pontos:
    print(ponto)

x_teclado = float(input("Digite o ponto para interpolação: "))

if x_teclado < pontos[0][0] or x_teclado > pontos[-1][0]:
    print("O ponto de interpolação está fora do intervalo fornecido.")
else:
    resultado_interpolado = calcula_por_lagrange(num_pontos, pontos, x_teclado)
    print(f"O valor interpolado em x = {x_teclado} é: {resultado_interpolado}")

