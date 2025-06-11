# Day 2: 30 Days of python programming

# Nombre y apellido 
first_name = 'Juan'  # Esto guarda tu nombre como texto
last_name = 'Pérez'   # Y esto tu apellido

# Nombre completo 
full_name = first_name + ' ' + last_name  # Une nombre y apellido con un espacio

# País y ciudad 
country = 'Argentina'
city = 'Buenos Aires'

# Edad y año 
age = 22
year = 2025

# Variables booleanas 
is_married = False
is_true = True
is_light_on = True

# Múltiples variables en una línea 
a, b, c = 1, 2, 3

# ---------- VERIFICANDO TIPOS DE DATOS ----------
print(type(first_name))    # <class 'str'>
print(type(age))           # <class 'int'>
print(type(is_married))    # <class 'bool'>
print(type(a))             # <class 'int'>


# len() cuenta cuántos caracteres tiene el nombre
print(len(first_name))

# Comparamos la longitud del nombre y del apellido
print(len(first_name) > len(last_name))  # Devuelve True o False

# ---------- OPERACIONES MATEMÁTICAS ----------
num_one = 5
num_two = 4

# Suma
total = num_one + num_two
# Resta
diff = num_one - num_two
# Multiplicación
product = num_one * num_two
# División normal
division = num_one / num_two
# Módulo (el resto de la división)
remainder = num_one % num_two
# Potencia (elevado a)
exp = num_one ** num_two
# División entera (sin decimales)
floor_division = num_one // num_two

# Mostramos todos los resultados
print("Total:", total)
print("Resta:", diff)
print("Multiplicación:", product)
print("División:", division)
print("Módulo:", remainder)
print("Potencia:", exp)
print("Floor Division:", floor_division)

# ---------- ÁREA Y CIRCUNFERENCIA DE UN CÍRCULO ----------
radius = 30
pi = 3.1416

# Área: π * r^2
area_of_circle = pi * radius ** 2
# Circunferencia: 2 * π * r
circum_of_circle = 2 * pi * radius

print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)

# ---------- INPUT DEL USUARIO ----------
# Pedimos datos al usuario (lo que escriba lo guardamos como texto)
nombre = input("Tu nombre: ")
apellido = input("Tu apellido: ")
pais = input("Tu país: ")
edad = int(input("Tu edad: "))  # Convertimos a número con int()

print("Hola", nombre, apellido, "de", pais, "con", edad, "años.")
