# Ejercicio 1.2

print("=" * 22)
print("Ejercicio 1\n")

edad = int(16)

if edad >= 16:
    print("Podes jugar \n")
else:
    print("No podes jugar \n")

print("=" * 18)
print("Ejercicio 2\n")

calificacion = int(input("Ingresa tu calificación (0-100): "))

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("Ay!, no aprobado")

# Ejercicio 2 con AND
print("Ejercicio con AND\n")

calificacion = int(input("Ingresa tu calificación (0-100): "))

if calificacion >= 90 and calificacion <= 100:
    print("Excelente")
elif calificacion >= 70 and calificacion < 90:
    print("Aprobado")
elif calificacion >= 0 and calificacion < 70:
    print("Ay!, no aprobado")

# Ejercicio 3

edad = int(input("¿Cuál es tu edad? "))
genero = input("¿Cuál es tu género favorito? (acción, comedia, terror): ").lower()

if edad < 13:
    print("Te recomendamos películas infantiles")

elif edad >= 13 and edad <= 17 and genero == "acción":
    print("Te recomendamos: Spider-Man (PG-13)")

elif edad >= 13 and edad <= 17 and genero == "comedia":
    print("Te recomendamos: Shrek (PG-13)")

elif edad >= 13 and edad <= 17 and genero == "terror":
    print("Te recomendamos: Scary Stories (PG-13)")

elif edad >= 18 and genero == "acción":
    print("Te recomendamos: John Wick")

elif edad >= 18 and genero == "comedia":
    print("Te recomendamos: Superbad")

elif edad >= 18 and genero == "terror":
    print("Te recomendamos: El Conjuro")
    