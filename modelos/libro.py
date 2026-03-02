class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Título y autor como tupla (inmutable)
        self._info = (titulo, autor)
        self._categoria = categoria
        self._isbn = isbn

    @property
    def titulo(self):
        return self._info[0]

    @property
    def autor(self):
        return self._info[1]

    @property
    def categoria(self):
        return self._categoria

    @property
    def isbn(self):
        return self._isbn

    def __str__(self):
        return f"{self.titulo} - {self.autor} | Categoría: {self.categoria} | ISBN: {self.isbn}"