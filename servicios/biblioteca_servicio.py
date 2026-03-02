from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    def __init__(self):
        # Diccionario ISBN -> Libro
        self._libros_disponibles = {}
        # Diccionario ID -> Usuario
        self._usuarios = {}
        # Set para IDs únicos
        self._ids_usuarios = set()

    # ================= LIBROS =================

    def añadir_libro(self, titulo, autor, categoria, isbn):
        if isbn in self._libros_disponibles:
            print("El ISBN ya existe.")
            return
        libro = Libro(titulo, autor, categoria, isbn)
        self._libros_disponibles[isbn] = libro
        print("Libro añadido correctamente.")

    def quitar_libro(self, isbn):
        if isbn in self._libros_disponibles:
            del self._libros_disponibles[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # ================= USUARIOS =================

    def registrar_usuario(self, nombre, user_id):
        if user_id in self._ids_usuarios:
            print("El ID ya está registrado.")
            return
        usuario = Usuario(nombre, user_id)
        self._usuarios[user_id] = usuario
        self._ids_usuarios.add(user_id)
        print("Usuario registrado correctamente.")

    def dar_baja_usuario(self, user_id):
        if user_id in self._usuarios:
            del self._usuarios[user_id]
            self._ids_usuarios.remove(user_id)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # ================= PRÉSTAMOS =================

    def prestar_libro(self, isbn, user_id):
        if isbn not in self._libros_disponibles:
            print("Libro no disponible.")
            return
        if user_id not in self._usuarios:
            print("Usuario no registrado.")
            return

        libro = self._libros_disponibles.pop(isbn)
        usuario = self._usuarios[user_id]
        usuario.prestar_libro(libro)
        print("Libro prestado correctamente.")

    def devolver_libro(self, isbn, user_id):
        if user_id not in self._usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self._usuarios[user_id]

        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.devolver_libro(libro)
                self._libros_disponibles[isbn] = libro
                print("Libro devuelto correctamente.")
                return

        print("El usuario no tiene ese libro.")

    # ================= BÚSQUEDA =================

    def buscar_por_titulo(self, titulo):
        for libro in self._libros_disponibles.values():
            if libro.titulo.lower() == titulo.lower():
                print(libro)

    def buscar_por_autor(self, autor):
        for libro in self._libros_disponibles.values():
            if libro.autor.lower() == autor.lower():
                print(libro)

    def buscar_por_categoria(self, categoria):
        for libro in self._libros_disponibles.values():
            if libro.categoria.lower() == categoria.lower():
                print(libro)

    def listar_libros_usuario(self, user_id):
        if user_id in self._usuarios:
            usuario = self._usuarios[user_id]
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print("Usuario no encontrado.")