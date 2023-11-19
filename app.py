

# Instalar con pip install mysql-connector-python
import mysql.connector




#--------------------------------------------------------------------
class Foro:
    #----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        # Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS participantes (
            codigo INT AUTO_INCREMENT PRIMARY KEY ,
            nombre VARCHAR(255) NOT NULL,
            alias VARCHAR(255) NOT NULL,
            residencia VARCHAR(255),
            destino VARCHAR(255),
            puntuacion INT,
            comentario VARCHAR(255))''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
        
    #----------------------------------------------------------------
    def agregar_participante(self, codigo, nombre, alias, residencia, destino, puntuacion,comentario):
        # Verificamos si ya existe un participante con el mismo código
        self.cursor.execute(f"SELECT * FROM participantes WHERE codigo = {codigo}")
        participante_existe = self.cursor.fetchone()
        if participante_existe:
            return False

        sql = "INSERT INTO participantes (codigo, nombre, alias, residencia, destino, puntuacion,comentario) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        valores = (codigo, nombre, alias, residencia, destino, puntuacion,comentario)

        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return True

    #----------------------------------------------------------------
    def consultar_participante(self, codigo):
        # Consultamos un participante a partir de su código
        self.cursor.execute(f"SELECT * FROM participantes WHERE codigo = {codigo}")
        return self.cursor.fetchone()

    #----------------------------------------------------------------
    def modificar_participante(self, codigo, nuevo_nombre, nuevo_alias, nuevo_residencia, nuevo_destino, nuevo_puntuacion,nuevo_comentario):
        sql = "UPDATE participantes SET nombre = %s, alias = %s, residencia = %s, destino = %s, puntuacion = %s, comentario %s WHERE codigo = %s"
        valores = (nuevo_nombre, nuevo_alias, nuevo_residencia, nuevo_destino, nuevo_puntuacion,nuevo_comentario, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def listar_participantes(self):
        self.cursor.execute("SELECT * FROM participantes")
        participantes = self.cursor.fetchall()
        return participantes

    #----------------------------------------------------------------
    def eliminar_participante(self, codigo):
        # Eliminamos un participante de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM participantes WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def mostrar_participante(self, codigo):
        # Mostramos los datos de un participante a partir de su código
        participante = self.consultar_participante(codigo)
        if participante:
            print("-" * 40)
            print(f"Código.....: {participante['codigo']}")
            print(f"Nombre: {participante['nombre']}")
            print(f"Alias...: {participante['alias']}")
            print(f"Recidencia.....: {participante['recidencia']}")
            print(f"Destino.....: {participante['destino']}")
            print(f"Puntuacion..: {participante['puntuacion']}")
            print(f"Comentario..: {participante['comentario']}")
            print("-" * 40)
        else:
            print("participante no encontrado.")

participantes=Foro("127.0.0.1","root","","mi_app")


