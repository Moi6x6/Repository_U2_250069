# 1. Declara tu edad como una variable entera
edad = 22

# 2. Declara tu altura como una variable flotante
altura = 1.78

# 3. Declara una variable que almacene un número complejo
numero_complejo = 2 + 3j

# 4. Área de un triángulo
base = float(input("Ingresa la base: "))
altura_triangulo = float(input("Ingresa la altura: "))
area_triangulo = 0.5 * base * altura_triangulo
print("El área del triángulo es", area_triangulo)

# 5. Perímetro de un triángulo
a = float(input("Ingresa el lado a: "))
b = float(input("Ingresa el lado b: "))
c = float(input("Ingresa el lado c: "))
perimetro = a + b + c
print("El perímetro del triángulo es", perimetro)

# 6. Área y perímetro de un rectángulo
largo = float(input("Ingresa el largo: "))
ancho = float(input("Ingresa el ancho: "))
area_rectangulo = largo * ancho
perimetro_rectangulo = 2 * (largo + ancho)
print("Área del rectángulo:", area_rectangulo)
print("Perímetro del rectángulo:", perimetro_rectangulo)

# 7. Área y circunferencia de un círculo
radio = float(input("Ingresa el radio: "))
pi = 3.14
area_circulo = pi * radio * radio
circunferencia = 2 * pi * radio
print("Área del círculo:", area_circulo)
print("Circunferencia del círculo:", circunferencia)

# 8. Pendiente, intersección con x e intersección con y de y = 2x - 2
pendiente = 2
interseccion_x = 2 / 2  # cuando y = 0 => 0 = 2x - 2 => x = 1
interseccion_y = -2     # cuando x = 0 => y = -2
print("Pendiente:", pendiente)
print("Intersección con x:", interseccion_x)
print("Intersección con y:", interseccion_y)

# 9. Pendiente y distancia euclidiana entre (2,2) y (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente_puntos = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Pendiente entre puntos:", pendiente_puntos)
print("Distancia euclidiana:", distancia)

# 10. Comparar pendientes
print("¿Las pendientes son iguales?:", pendiente == pendiente_puntos)

# 11. Valor de y = x^2 + 6x + 9
valores_x = [-3, 0, 1, -6]
for x in valores_x:
    y = x**2 + 6*x + 9
    print(f"x={x} => y={y}")

# 12. Longitud y comparación falsa
print(len("python") != len("dragon"))

# 13. 'on' en ambas palabras
print("on" in "python" and "on" in "dragon")

# 14. Verificar 'jargon' en una oración
oracion = "I hope this course is not full of jargon."
print("jargon" in oracion)

# 15. Afirmación falsa sobre 'on'
print("on" not in "python" and "on" not in "dragon")

# 16. Convertir longitud a float y a string
longitud_py = len("python")
print(float(longitud_py))
print(str(longitud_py))

# 17. Verificar si un número es par
num = int(input("Ingresa un número para verificar si es par o impar: "))
print("¿Es par?:", num % 2 == 0)

# 18. Verificar división entera
print(7 // 3 == int(2.7))

# 19. Verificar tipos
print(type('10') == type(10))

# 20. int('9.8') == 10 dará error, se arregla con float
print(int(float('9.8')) == 10)

# 21. Calcular salario
horas = float(input("Ingresa las horas trabajadas: "))
rata = float(input("Ingresa la tarifa por hora: "))
salario = horas * rata
print("Tu ganancia semanal es", salario)

# 22. Años a segundos
años = int(input("Ingresa los años que has vivido: "))
segundos_vividos = años * 365 * 24 * 60 * 60
print(f"Has vivido {segundos_vividos} segundos.")

# 23. Mostrar tabla
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)