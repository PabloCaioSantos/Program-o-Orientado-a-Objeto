import math
import random

escolha = input("Qual tipo de triângulo você quer? (Equilátero, Isósceles ou Escaleno): ")

while True:
    x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
    x2, y2 = random.randint(-10, 10), random.randint(-10, 10)
    x3, y3 = random.randint(-10, 10), random.randint(-10, 10)

    lado1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    lado2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    lado3 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

    area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2

    if area != 0:  # não pode ser pontos alinhados
        if lado1 == lado2 and lado2 == lado3:
            tipo = "Equilátero"
        elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            tipo = "Isósceles"
        else:
            tipo = "Escaleno"

        if tipo.lower() == escolha.lower():
            print(f"Triângulo {tipo} encontrado!")
            print(f"P1 = ({x1}, {y1})")
            print(f"P2 = ({x2}, {y2})")
            print(f"P3 = ({x3}, {y3})")
            break