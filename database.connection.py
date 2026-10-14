import sqlite3
import os


class DatabaseConnection:
    """Maneja la conexión con la base de datos SQLite."""

    # Ruta al archivo .db (dentro de la carpeta database/)
    DB_PATH = os.path.join(os.path.dirname(__file__), 'foodiego.db')

    @classmethod
    def get_connection(cls):
        """Devuelve una conexión activa a la BD."""
        return sqlite3.connect(cls.DB_PATH)

    @classmethod
    def execute_query(cls, query, params=()):
        """Ejecuta una consulta SQL y devuelve el cursor."""
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return conn, cursor  # Devolvemos ambos para poder cerrar después

    @classmethod
    def initialize_tables(cls):
        """Crea todas las tablas si no existen."""
        # Aquí irá el script adaptado (lo veremos en la Fase 2)
        pass
