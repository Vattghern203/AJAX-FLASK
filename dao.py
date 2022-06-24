from models import Manga

SQL_ADD_MANGA = 'INSERT INTO MANGA (NOME, CAPS, VOLUMES, AUTOR, ANO) VALUES (?, ?, ?, ?, ?)'

SQL_BUSCA_MANGA = 'SELECT * FROM MANGA'


class MangaDao:
    def __init__(self, db):
        self.__db = db


    def add_manga(self, manga:Manga):
        cursor = self.__db.cursor()

        cursor.execute(SQL_ADD_MANGA, (manga._nome, manga._caps, manga._volumes, manga._autor, manga._ano))

        self.__db.commit()

        return manga

    
    def listar_manga(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_BUSCA_MANGA)
        mangas = traduz_mangas(cursor.fetchall())
        return mangas

def traduz_mangas(mangas):
    def cria_mangas_com_tupla(tupla):
        return Manga(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], id=tupla[0])
    return list(map(cria_mangas_com_tupla, mangas))