import math

def ler_dados_de_arquivo():
    with open("entrada-pontos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    n = int(linhas[0])
    pontosXY = []

    for i in range(1, n + 1):
        pontos = list(map(float, linhas[i].split()))
        pontosXY.append(pontos)
    
    return n, pontosXY



def calcular_regra_retangulo_simples(pontos):
    a, b = pontos[0][0], pontos[-1][0]
    h = b - a
    fx_a = pontos[0][1]
    integral = h * fx_a
    return integral

def calcular_regra_trapezio_simples(pontos):
    a, b = pontos[0][0], pontos[-1][0]
    h = b - a
    fx_a = pontos[0][1]
    fx_b = pontos[-1][1]
    integral = h * (fx_a + fx_b) / 2
    return integral


def calcular_regra_1_3_simpson_simples(pontos):
    a, b = pontos[0][0], pontos[-1][0]
    h = (b - a) / 2
    fx_a = pontos[0][1]
    fx_b = pontos[-1][1]
    fx_mid = pontos[len(pontos) // 2][1]
    integral = (h / 3) * (fx_a + 4 * fx_mid + fx_b)
    return integral

def calcular_regra_3_8_simpson_simples(pontos):
    a, b = pontos[0][0], pontos[-1][0]
    h = (b - a) / 3
    fx_a = pontos[0][1]
    fx_b = pontos[-1][1]
    fx_mid1 = pontos[len(pontos) // 3][1]
    fx_mid2 = pontos[2 * len(pontos) // 3][1]
    integral = (3 * h / 8) * (fx_a + 3 * fx_mid1 + 3 * fx_mid2 + fx_b)
    return integral


def calcular_regra_retangulo_composta(pontos, n):
    a, b = pontos[0][0], pontos[-1][0]
    h = (b - a) / n
    integral = 0

    for i in range(n):
        x_i = a + i * h
        fx_i = 0

        for ponto in pontos:
            if ponto[0] == x_i:
                fx_i = ponto[1]
                break

        integral += h * fx_i

    return integral




def calcular_regra_gaussiana_n2(pontos):
    a, b = pontos[0][0], pontos[-1][0]
    c1 = 1
    c2 = 1
    x1 = -math.sqrt(3) / 3 
    x2 = math.sqrt(3) / 3 

    integral = ((b - a) / 2) * (
            c1 * pontos[0][1] * (1 / math.sqrt(1 - x1**2) ) + c2 * pontos[-1][1] * (1 / math.sqrt(1 - x2**2))
        )

    return integral


def calcular_regra_gaussiana_n3(pontos):
    a, b = pontos[0][0], pontos[-1][0]
    c1 = 5 / 9
    c2 = 8 / 9
    c3 = 5 / 9
    x1 = - math.sqrt(3 / 5)
    x2 = 0
    x3 = math.sqrt(3 / 5)

    ponto_meio = len(pontos) // 2
    integral = ((b - a) / 2) * (c1 * pontos[0][1] * (1 / math.sqrt(1 - x1**2) ) + c2 * pontos[ponto_meio][1] * (1 / math.sqrt(1 - x2**2)) + c3 * pontos[-1][1] * (1 / math.sqrt(1 - x3**2)))

    return integral


def calcular_regra_gaussiana_n4(pontos):
    a, b = pontos[0][0], pontos[-1][0]
    c1 = (18 + math.sqrt(30)) / 36
    c2 = (18 - math.sqrt(30)) / 36
    x1 = - math.sqrt((3 + 2 * math.sqrt(6 / 5)) / 7)
    x2 = - math.sqrt((3 - 2 * math.sqrt(6 / 5)) / 7)
    x3 = math.sqrt((3 - 2 * math.sqrt(6 / 5)) / 7)
    x4 = math.sqrt((3 + 2 * math.sqrt(6 / 5)) / 7)

    ponto_meio = len(pontos) // 3 # 1/3 do intervalo

    integral = ((b - a) / 2) * (c1 * pontos[0][1] * (1 / math.sqrt(1 - x1**2)) + c2 * pontos[ponto_meio][1] * (1 / math.sqrt(1 - x2**2)) + c2 * pontos[ponto_meio][1] * (1 / math.sqrt(1 - x3**2)) + c1 * pontos[-1][1] * (1 / math.sqrt(1 - x4**2)))

    return integral



num_pontos, pontos = ler_dados_de_arquivo()

print("Pontos lidos:")
for ponto in pontos:
    print(ponto)


integral = calcular_regra_retangulo_simples(pontos)
print(f"A integral usando a regra do retangulo simples é: {integral}")

integral = calcular_regra_trapezio_simples(pontos)
print(f"A integral usando a regra do trapezio simples é: {integral}")


integral = calcular_regra_1_3_simpson_simples(pontos)
print(f"A integral usando a regra de Simpson 1/3 é: {integral}")

integral = calcular_regra_3_8_simpson_simples(pontos)
print(f"A integral usando a regra de Simpson 3/8 é: {integral}")


integral = calcular_regra_trapezio_simples(pontos)
print(f"A integral usando a regra do trapezio simples é: {integral}")

integral = calcular_regra_retangulo_composta(pontos, 10)
print(f"A integral usando a regra do retangulo composto com n=10 é: {integral}")

integral = calcular_regra_retangulo_composta(pontos, 100)
print(f"A integral usando a regra do retangulo composto com n=100 é: {integral}")

integral = calcular_regra_retangulo_composta(pontos, 1000)
print(f"A integral usando a regra do retangulo composto com n=1000 é: {integral}")

integral = calcular_regra_gaussiana_n2(pontos)
print(f"A integral usando Gaussiana com n=2 é: {integral}")

integral = calcular_regra_gaussiana_n3(pontos)
print(f"A integral usando Gaussiana com n=3 é: {integral}")

integral = calcular_regra_gaussiana_n4(pontos)
print(f"A integral usando Gaussiana com n=4 é: {integral}")
