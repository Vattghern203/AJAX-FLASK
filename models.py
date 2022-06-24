class Manga:
    def __init__(self, nome, caps, volumes, autor, ano, id=None) -> None:
        self._id = id
        self._nome = nome
        self._caps = caps
        self._volumes = volumes
        self._autor = autor
        self._ano = ano        