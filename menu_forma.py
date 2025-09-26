import math

while True:
    print("\n--- MENU ---")
    print("1 - Identificar tipo de triângulo")
    print("2 - Identificar quadrilátero")
    print("3 - Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        # --- Algoritmo do Triângulo ---
        x1 = float(input("Digite x1: "))
        y1 = float(input("Digite y1: "))

        x2 = float(input("Digite x2: "))
        y2 = float(input("Digite y2: "))

        x3 = float(input("Digite x3: "))
        y3 = float(input("Digite y3: "))

        lado1 = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
        lado2 = int(math.sqrt((x3 - x2)**2 + (y3 - y2)**2))
        lado3 = int(math.sqrt((x1 - x3)**2 + (y1 - y3)**2))

        # Verificar se os pontos são colineares (área = 0)
        area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2

        if area == 0:
            print("Os pontos não formam um triângulo.")
        else:
            if lado1 == lado2 and lado2 == lado3:
                print("O triângulo é Equilátero.")
            elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
                print("O triângulo é Isósceles.")
            else:
                print("O triângulo é Escaleno.")

    elif escolha == "2":
        # --- Algoritmo do Quadrilátero ---
        x1 = float(input("Digite x1 de A: "))
        y1 = float(input("Digite y1 de A: "))

        x2 = float(input("Digite x2 de B: "))
        y2 = float(input("Digite y2 de B: "))

        x3 = float(input("Digite x3 de C: "))
        y3 = float(input("Digite y3 de C: "))

        x4 = float(input("Digite x4 de D: "))
        y4 = float(input("Digite y4 de D: "))

        AB = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        BC = math.sqrt((x3-x2)**2 + (y3-y2)**2)
        CD = math.sqrt((x4-x3)**2 + (y4-y3)**2)
        DA = math.sqrt((x1-x4)**2 + (y1-y4)**2)

        AC = math.sqrt((x3-x1)**2 + (y3-y1)**2)
        BD = math.sqrt((x4-x2)**2 + (y4-y2)**2)

        dot1 = (x2-x1)*(x3-x2) + (y2-y1)*(y3-y2)  # Ângulo em B
        dot2 = (x3-x2)*(x4-x3) + (y3-y2)*(y4-y3)  # Ângulo em C
        dot3 = (x4-x3)*(x1-x4) + (y4-y3)*(y1-y4)  # Ângulo em D
        dot4 = (x1-x4)*(x2-x1) + (y1-y4)*(y2-y1)  # Ângulo em A

        if abs(dot1) < 1e-6 and abs(dot2) < 1e-6 and abs(dot3) < 1e-6 and abs(dot4) < 1e-6:
            if abs(AB-BC) < 1e-6 and abs(BC-CD) < 1e-6 and abs(CD-DA) < 1e-6:
                print("Quadrado")
            else:
                print("Retângulo")
        else:
            if abs(AB-BC) < 1e-6 and abs(BC-CD) < 1e-6 and abs(CD-DA) < 1e-6:
                print("Losango")
            elif abs(AB-CD) < 1e-6 and abs(BC-DA) < 1e-6:
                print("Paralelogramo")
            elif abs(AB-CD) < 1e-6 or abs(BC-DA) < 1e-6:
                print("Trapézio")
            else:
                print("Quadrilátero qualquer")

    elif escolha == "3":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")
