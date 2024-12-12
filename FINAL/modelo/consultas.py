from.coneccion import ConeccionDB

def crear_tabla():
    conexion = ConeccionDB()

    sql="""
            CREATE TABLE IF NOT EXISTS Genero(
            ID INTEGER NOT NULL,
            Nombre VARCHAR(50),
            PRIMARY KEY (ID AUTOINCREMENT)
            );
    
            CREATE TABLE IF NOT EXISTS Peliculas(
            ID INTEGER NOT NULL,
            Nombre VARCHAR(150),
            Duracion VARCHAR(4),
            Genero INTEGER,
            PRIMARY KEY (ID AUTOINCREMENT),
            FOREIGN KEY (Genero) REFERENCES Genero(ID)
            );
            """
    
    try:
        conexion.cursor.execute(sql)
    except:
        pass
    finally:
        conexion.cerrar_coneccion()


class Peliculas:
    def __init__(self, nombre, duracion, genero):
        self.id_peliclas = None
        self.nombre = nombre
        self.duracion = duracion    
        self.genero = genero

    def __str__(self):
        return f'Pelicula[{self.nombre},{self.duracion},{self.genero}]'
    
def guardar_pelicula(Pelicula):
    conexion = ConeccionDB()
    sql = f"""
            INSERT INTO Peliculas (Nombre,Duracion,Genero)
            VALUES ('{Pelicula.nombre}','{Pelicula.duracion}',{Pelicula.genero})
            """
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_coneccion()
    except:
        pass


def listar_peliculas():
    conexion = ConeccionDB()
    lista_peliculas = []

    sql = f"""
            SELECT * FROM Peliculas as p
            INNER JOIN Genero as g
            ON p.Genero = g.ID;
            """
    
    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar_coneccion()
        return lista_peliculas
    except:
        pass


def lista_generos():
    conexion = ConeccionDB()
    listar_generos = []
    sql = f"""
            SELECT * FROM Genero;
    """
    try:
        conexion.cursor.execute(sql)
        listar_generos = conexion.cursor.fetchall()
        conexion.cerrar_coneccion()
        return listar_generos
    except:
        pass

def editar_pelicula(Pelicula, id):
    conexion = ConeccionDB()
    sql = f"""
            UPDATE Peliculas 
            SET Nombre = '{Pelicula.nombre}', Duracion = '{Pelicula.duracion}',
            Genero = {Pelicula.genero})
            WHERE ID = {id};
            """
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_coneccion()
    except:
        pass

def borrar_pelicula(Pelicula, id):
    conexion = ConeccionDB()
    sql = f"""
            DELETE FROM Peliculas 
            WHERE ID = {id};
            """
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_coneccion()
    except:
        pass