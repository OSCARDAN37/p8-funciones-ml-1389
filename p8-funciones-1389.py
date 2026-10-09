# Oscar Flores NC = 1389
# UI Act 11 Estructuras de datos y funciones
print("-+-+-+-+-+-+- Ejemplo 1 -+-+-+-+-+-+-")
def saludar():
    print("¡Hola, mundo!")

# Llamar a la función
saludar()
# Salida: ¡Hola, mundo!
print("-+-+-+-+-+-+- Ejemplo 2 -+-+-+-+-+-+-")
def imprimir_mensaje(mensaje):
    print(mensaje)
    # No hay return

resultado = imprimir_mensaje("Hola")
print(resultado)  # None
print("-+-+-+-+-+-+- Ejemplo 3 -+-+-+-+-+-+-")
def calcular_area_rectangulo(ancho, alto):
    """Calcula el área de un rectángulo"""
    area = ancho * alto
    return area

# Llamar a la función
resultado = calcular_area_rectangulo(5, 10)
print(resultado)  # Salida: 50

# El orden importa
resultado2 = calcular_area_rectangulo(10, 5)
print(resultado2)  # Salida: 50 (mismo resultado en este caso)
print("-+-+-+-+-+-+- Ejemplo 4 -+-+-+-+-+-+-")
def crear_usuario(nombre, edad, ciudad):
    return f"{nombre}, {edad} años, de {ciudad}"

# Usando parámetros posicionales
usuario1 = crear_usuario("Ana", 25, "Madrid")

# Usando parámetros con nombre (más claro)
usuario2 = crear_usuario(nombre="Carlos", edad=30, ciudad="Barcelona")

# Puedes cambiar el orden si usas nombres
usuario3 = crear_usuario(ciudad="Valencia", nombre="Laura", edad=28)

print(usuario1)  # Ana, 25 años, de Madrid
print(usuario2)  # Carlos, 30 años, de Barcelona
print(usuario3)  # Laura, 28 años, de Valencia
print("-+-+-+-+-+-+- Ejemplo 5 -+-+-+-+-+-+-")
def saludar(nombre, saludo="Hola"):
    """Saluda a una persona con un saludo personalizable"""
    return f"{saludo}, {nombre}!"

print(saludar("María"))  # Hola, María!
print(saludar("Pedro", "Buenos días"))  # Buenos días, Pedro!
print(saludar("Ana", saludo="Qué tal"))  # Qué tal, Ana!
print("-+-+-+-+-+-+- Ejemplo 6 -+-+-+-+-+-+-")
def calcular_estadisticas(numeros):
    """Calcula suma, promedio y máximo de una lista"""
    total = sum(numeros)
    promedio = total / len(numeros)
    maximo = max(numeros)
    return total, promedio, maximo  # Devuelve una tupla

# Desempaquetado de valores
suma, prom, max_val = calcular_estadisticas([10, 20, 30, 40, 50])
print(f"Suma: {suma}, Promedio: {prom}, Máximo: {max_val}")
# Salida: Suma: 150, Promedio: 30.0, Máximo: 50
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
print("Programa realizado por Oscar Flores NC = 1389")