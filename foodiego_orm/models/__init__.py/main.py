DatabaseConnection.initialize_tables()

# Crear un cliente
cliente1 = Cliente(
    nombre="Ana",
    apellido="Gómez",
    email="ana@email.com",
    telefono="555-1234",
    direccion_entrega="Calle Falsa 123"
)

# Guardarlo
cliente1.save()

# CREATE: Pasar los campos como kwargs
c1 = Cliente(
    nombre="Ana",
    apellido="Gómez",
    email="ana@email.com",
    telefono="555-1234",
    direccion_entrega="Calle Falsa 123"
)
c1.save()

c2 = Cliente(
    nombre="Luis",
    apellido="Pérez",
    email="luis@email.com",
    telefono="555-5678",
    direccion_entrega="Calle 2"
)
c2.save()

# READ: Ahora funciona sin errores
print("\n--- Todos los clientes ---")
todos = Cliente.all()
for cliente in todos:
    print(f"ID: {cliente.id_cliente}, Nombre: {cliente.nombre} {cliente.apellido}")
    print(f" Email: {cliente.email}, Fecha registro: {cliente.fecha_registro}")

# READ: Buscar por ID
print("\n--- Buscar cliente ID 1 ---")
cliente_buscado = Cliente.find_by_id(1)
print(f"Email: {cliente_buscado.email}")

# UPDATE
c1.update(telefono="555-9999")

print("\n--- Después del UPDATE ---")
for c in Cliente.all():
    print(f"{c.id_cliente}: {c.nombre} - {c.telefono}")

# DELETE
c1.delete()

print("\n--- Después del DELETE ---")
for c in Cliente.all():
    print(f"{c.id_cliente}: {c.nombre}")