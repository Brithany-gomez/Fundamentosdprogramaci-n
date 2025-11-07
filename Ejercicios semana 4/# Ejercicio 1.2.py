# Ejercicio 1.2

print("\nEjercicio 1")
canciones = ["As it was","Flowers", "Vampire" , "Cruel summer" , "Calm down"]
print("MIS CANCIONES FAVORITAS:")
print(canciones[0])
print(canciones[1])
print(canciones[2])
print(canciones[3])
print(canciones[4])

# Ejercicio 2

print("\nEjercicio 2\n")
amigos = []

print ("Lista inicial:", amigos)

amigos.append ("Andrea")
print("Despues de agregar a Andrea:", amigos)

amigos.append ("Meli")
print("Despues de agregar a Meli:", amigos)

amigos.append ("Xime")
print("Despues de agregar a Xime:", amigos)

print(f"\nTotal de amigos: {len(amigos)}")

# Ejercicio 3

print("\nEjercicio 3\n")
calificaciones = [98, 90, 92, 89]

#Mostrar todas las calificaciones
print("Tus calificaciones:", calificaciones)

#Calcular el promedio
suma = sum(calificaciones)
promedio = suma / len(calificaciones)
print(f"Promedio: {promedio}")

#Encontrar la mejor y peor calificacion
mejor = max(calificaciones)
peor = min(calificaciones)
print(f"Mejor calificacion: {mejor}")
print(f"Peor calificacion: {peor}")

# Ejercicio 4

print("\nEjercicio 4\n")
carrito = []
# Agregar productos
print("🛍 Agregando productos al carrito...")
carrito.append("iPhone 15")
carrito.append("AirPods")
carrito.append("Funda")
carrito.append("Cargador")

print("Carrito actual:", carrito)
print(f"Productos en el carrito: {len(carrito)}")

# Decidiste que no quieres la funda
print("\n❌ Eliminando la funda...")
carrito.remove("Funda")

print("Carrito final:", carrito)
print(f"Total de productos: {len(carrito)}")

# Ejercicio 5

print("\nEjercicio 5\n")

videojuegos = ["Minecraft", "Fortnite", "Valorant", "Roblox", "GTA V"]

print("🎮 MI TOP 5 DE VIDEOJUEGOS:")
print(videojuegos)

# Mostrar el primero y el último
print(f"\nMi favorito (posición 0): {videojuegos[0]}")
print(f"El de la posición 5 (último): {videojuegos[-1]}")

# Cambiar mi juego favorito
print("\n🔄 Cambio de opinión...")
videojuegos[0] = "Apex Legends"

print("Top 5 actualizado:")
print(videojuegos)

# Ejercicio 6

print("\nEjercicio 6\n")
series = ["Stranger Things", "Wednesday", "The Last of Us"]

print("📺 Series para ver:", series)

# Agregar una nueva serie
series.append("One Piece")
print("Agregaste One Piece:", series)

# Verificar si una serie está en tu lista
if "Wednesday" in series:
    print("\n✅ Sí tienes Wednesday en tu lista")

if "Breaking Bad" in series:
    print("Tienes Breaking Bad")
else:
    print("❌ No tienes Breaking Bad en tu lista")

# Ya viste la primera serie, la eliminas
print(f"\n¡Terminaste de ver! {series[0]}!")
series.pop(0)
print("Series restantes:", series)