class Usuario:
    def __init__(self, nombre, user_id):
        self._nombre = nombre
        self._user_id = user_id
        # Lista para libros prestados
        self._libros_prestados = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def user_id(self):
        return self._user_id

    @property
    def libros_prestados(self):
        return self._libros_prestados

    def prestar_libro(self, libro):
        self._libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self._libros_prestados:
            self._libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.nombre} | ID: {self.user_id}"