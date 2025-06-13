# 1. Declaré una lista vacía
lista_vacia = []

# 2. Declaré una lista con más de 5 elementos
cosas = ['libro', 'ratón', 'teclado', 'cuaderno', 'botella', 'teléfono']

# 3. Obtuve la longitud de la lista
print(len(cosas))

# 4. Primer, medio y último elemento
print("Primer elemento:", cosas[0])
print("Elemento del medio:", cosas[len(cosas)//2])
print("Último elemento:", cosas[-1])

# 5. Lista con diferentes tipos de datos
datos_personales = ['MiNombre', 21, 1.78, 'Soltero', 'Ciudad Ejemplo']

# 6. Lista de empresas de tecnología
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Imprimí la lista
print(it_companies)

# 8. Cantidad de empresas
print("Número de empresas:", len(it_companies))

# 9. Primera, del medio y última empresa
print("Primera empresa:", it_companies[0])
print("Empresa del medio:", it_companies[len(it_companies)//2])
print("Última empresa:", it_companies[-1])

# 10. Modifiqué una empresa
it_companies[1] = 'Alphabet'
print(it_companies)

# 11. Agregué una empresa al final
it_companies.append('Spotify')
print(it_companies)

# 12. Inserté una empresa en el medio
it_companies.insert(len(it_companies)//2, 'Netflix')
print(it_companies)

# 13. Cambié una empresa a mayúsculas (excepto IBM)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14. Uní las empresas con un separador
print('#; '.join(it_companies))

# 15. Verifiqué si existe una empresa
print('Google' in it_companies)
print('Spotify' in it_companies)

# 16. Ordené la lista alfabéticamente
it_companies.sort()
print(it_companies)

# 17. Invertí el orden de la lista
it_companies.reverse()
print(it_companies)

# 18. Corté las primeras 3 empresas
print(it_companies[:3])

# 19. Corté las últimas 3 empresas
print(it_companies[-3:])

# 20. Corté la(s) empresa(s) del medio
medio = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print(it_companies[medio-1:medio+1])
else:
    print(it_companies[medio])

# 21. Eliminé la primera empresa
it_companies.pop(0)
print(it_companies)

# 22. Eliminé la(s) del medio
medio = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[medio-1:medio+1]
else:
    del it_companies[medio]
print(it_companies)

# 23. Eliminé la última empresa
it_companies.pop()
print(it_companies)

# 24. Eliminé todas las empresas
it_companies.clear()
print(it_companies)

# 25. Destruí la lista por completo
del it_companies

# 26. Uní listas de frontend y backend
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27. Inserté Python y SQL después de Redux
indice_redux = full_stack.index('Redux')
full_stack[indice_redux + 1:indice_redux + 1] = ['Python', 'SQL']
print(full_stack)

## Nivel 2 
# 1. Lista de edades
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordené la lista y encontré la edad mínima y máxima
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Edades ordenadas:", ages)
print("Edad mínima:", min_age)
print("Edad máxima:", max_age)

# Agregué nuevamente la edad mínima y máxima a la lista
ages.extend([min_age, max_age])
print("Lista con min y max duplicados:", ages)

# Calcular la mediana
ages.sort()
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
print("Mediana:", median)

# Calcular el promedio
average = sum(ages) / len(ages)
print("Promedio:", average)

# Calcular el rango
range_ages = max(ages) - min(ages)
print("Rango:", range_ages)

# Comparé la diferencia absoluta entre min-prom y max-prom
print("abs(min - promedio):", abs(min_age - average))
print("abs(max - promedio):", abs(max_age - average))

# ya trabjado con la lista de paises 
# Para estos ejercicios, uso una lista de ejemplo (puedes cargarla desde countries.py si quieres)
countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia',
    'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados',
    'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
    'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi'
]  # <- Lista de ejemplo con 27 países

# 1. Encontrar el/los país(es) del medio
middle = len(countries) // 2
if len(countries) % 2 == 0:
    print("Países del medio:", countries[middle - 1], "y", countries[middle])
else:
    print("País del medio:", countries[middle])

# 2. Dividir la lista en dos mitades
if len(countries) % 2 == 0:
    first_half = countries[:middle]
    second_half = countries[middle:]
else:
    first_half = countries[:middle+1]
    second_half = countries[middle+1:]
print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)

# 3. Desempaquetado de países
lista_paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
primero, segundo, tercero, *scandic_countries = lista_paises
print("Primeros países:", primero, segundo, tercero)
print("Países escandinavos:", scandic_countries)
