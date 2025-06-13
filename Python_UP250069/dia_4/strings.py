# 1. Une las palabras en una sola cadena
print(' '.join(['Thirty', 'Days', 'Of', 'Python']))

# 2. Une las palabras en una sola cadena
print(' '.join(['Coding', 'For', 'All']))

# 3. Declara una variable
empresa = "Coding For All"

# 4. Imprime la variable
print(empresa)

# 5. Imprime la longitud (cantidad de caracteres)
print(len(empresa))

# 6. Convierte todo a mayúsculas
print(empresa.upper())

# 7. Convierte todo a minúsculas
print(empresa.lower())

# 8. Diferentes formas de formatear el texto
print(empresa.capitalize())   # Primera letra mayúscula
print(empresa.title())        # Primera letra de cada palabra en mayúscula
print(empresa.swapcase())     # Cambia mayúsculas ↔ minúsculas

# 9. Corta la primera palabra (deja "For All")
print(empresa[7:])

# 10. Verifica si contiene la palabra "Coding"
print('Coding' in empresa)
print(empresa.find('Coding'))
print(empresa.index('Coding'))

# 11. Reemplaza "Coding" por "Python"
print(empresa.replace('Coding', 'Python'))

# 12. Cambia "Python for Everyone" por "Python for All"
print("Python for Everyone".replace("Everyone", "All"))

# 13. Divide la cadena por espacios
print(empresa.split())

# 14. Divide la cadena por comas
empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(empresas.split(", "))

# 15. Caracter en el índice 0
print(empresa[0])

# 16. Último índice
print(len(empresa) - 1)

# 17. Caracter en el índice 10
print(empresa[10])

# 18. Acrónimo de 'Python For Everyone'
nombre1 = "Python For Everyone"
acronimo1 = ''.join([palabra[0] for palabra in nombre1.split()])
print(acronimo1)  # PFE

# 19. Acrónimo de 'Coding For All'
nombre2 = "Coding For All"
acronimo2 = ''.join([palabra[0] for palabra in nombre2.split()])
print(acronimo2)  # CFA

# 20. Posición de la primera 'C'
print(empresa.index('C'))

# 21. Posición de la primera 'F'
print(empresa.index('F'))

# 22. Última posición de 'l' (minúscula) en la frase
frase = "Coding For All People"
print(frase.rfind('l'))

# 23. Posición de la primera aparición de 'because'
frase_because = 'You cannot end a sentence with because because because is a conjunction'
print(frase_because.find('because'))

# 24. Última aparición de 'because'
print(frase_because.rindex('because'))

# 25 y 27. Recorta 'because because because'
inicio = frase_because.find('because')
final = frase_because.rindex('because') + len('because')
print(frase_because[inicio:final])

# 26. Posición de la primera 'because'
print(frase_because.find('because'))

# 28. ¿Empieza con "Coding"?
print(empresa.startswith('Coding'))

# 29. ¿Termina con "coding"?
print(empresa.endswith('coding'))

# 30. Elimina espacios en los extremos
texto = "   Coding For All     "
print(texto.strip())

# 31. ¿Cuál es un identificador válido?
print("30DaysOfPython".isidentifier())       # False
print("thirty_days_of_python".isidentifier())  # True

# 32. Une la lista con #
librerías = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(librerías))

# 33. Usa salto de línea
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Usa tabulaciones
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35. Formateo con variables
radio = 10
area = 3.14 * radio ** 2
print(f'El área de un círculo con radio {radio} es {int(area)} metros cuadrados.')

# 36. Formateo de operaciones
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
