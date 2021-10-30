from dominio import *
from servicio import *


opcion = None
while opcion != 4:
    try:
        print("Opciones.")
        print("1. Agregar pelicula")
        print("2. Listar pelicula")
        print("3. Eliminar pelicula")
        print("4. Salir")

        opcion = int(input("Escribe tu opcion entre 1 y 4:  "))

        if opcion == 1:
            nombre_pelicula = input("Proporciona el nombre de la pelicula: ")
            pelicula = Pelicula(nombre_pelicula)
            Catalogo.agregar_pelicula(pelicula)

        elif opcion == 2:
            Catalogo.listar_peliculas()
        elif opcion == 3:
            Catalogo.eliminar_peliculas()



    except Exception as e:
        print(f"Ocurrio un error {e}")
        opcion = None
else:
    print("Salimos del programa...")