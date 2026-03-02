from servicios.biblioteca_servicio import BibliotecaServicio

def menu():
    biblioteca = BibliotecaServicio()

    while True:
        print("\n=== SISTEMA BIBLIOTECA DIGITAL ===")
        print("1. Añadir libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar libro por título")
        print("6. Listar libros de usuario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.añadir_libro(titulo, autor, categoria, isbn)

        elif opcion == "2":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID del usuario: ")
            biblioteca.registrar_usuario(nombre, user_id)

        elif opcion == "3":
            isbn = input("ISBN del libro: ")
            user_id = input("ID del usuario: ")
            biblioteca.prestar_libro(isbn, user_id)

        elif opcion == "4":
            isbn = input("ISBN del libro: ")
            user_id = input("ID del usuario: ")
            biblioteca.devolver_libro(isbn, user_id)

        elif opcion == "5":
            titulo = input("Título a buscar: ")
            biblioteca.buscar_por_titulo(titulo)

        elif opcion == "6":
            user_id = input("ID del usuario: ")
            biblioteca.listar_libros_usuario(user_id)

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()