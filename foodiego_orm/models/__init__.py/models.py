form models.base_model import Model
from database.connection import DatabaseConnection

class Cliente(Model):
    table_name = "clientes"
    primary_key = "id_cliente"
    fields = ["nombre", "apellido, "email","telefono", "direccion_entrega]
    def __init__(self, **kwargs):
    super().__init__(**kwargs)
    def save(self):
    columns = ", ".join(self.fields)
    placeholders = ", ".join(["?" for _ in self.fields]) 
    values = tuple(getattr(self, field) for field in self.fields)
    query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
    conn, cursor = DatabaseConnection.execute_query(query, values)
    self.id_cliente = cursor.lastrowid
    conn.close()
    print(f"Cliente '{self.nombre}' guardado con ID {self.id_cliente}.")
    
