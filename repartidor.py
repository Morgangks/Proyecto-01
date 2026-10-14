import tkinter as tk
from tkinter import messagebox
from views.form_base import FormBase
from models.repartidor import Repartidor
 
 
class RepartidorView(FormBase):
    
 
    titulo = "Gestión de Repartidores"
    columnas_tabla = ("ID", "Nombre", "Apellido", "Vehículo", "Placa", "Estado")
    ancho_columnas = (40, 130, 130, 100, 90, 100)
 
    campos_formulario = (
        {"nombre": "nombre", "etiqueta": "Nombre", "tipo": "entry"},
        {"nombre": "apellido", "etiqueta": "Apellido", "tipo": "entry"},
        {"nombre": "tipo_vehiculo", "etiqueta": "Vehículo", "tipo": "combobox",
         "valores": ("Bicicleta", "Moto", "Auto", "Patineta eléctrica")},
        {"nombre": "placa", "etiqueta": "Placa", "tipo": "entry"},
    )
 
    def __init__(self, parent):
        
        self.estado_var = tk.StringVar(value="disponible")
        super().__init__(parent, Repartidor)
      
        self.geometry("850x620")
 
    def _crear_formulario(self):
        
        super()._crear_formulario()  
 
        frame_estado = tk.LabelFrame(
            self, text=" Estado del Repartidor ",
            font=("Arial", 10, "bold"),
            bg="#ecf0f1", padx=10, pady=5
        )
        frame_estado.pack(fill="x", padx=10, pady=5)
 
    
        estados = [("Disponible", "disponible"), ("En ruta", "en_ruta")]
        for texto, valor in estados:
            tk.Radiobutton(
                frame_estado, text=texto, value=valor,
                variable=self.estado_var,
                font=("Arial", 9), bg="#ecf0f1"
            ).pack(side="left", padx=10)
 
    def _cargar_en_formulario(self, datos):
        
        self.entries["nombre"].delete(0, tk.END)
        self.entries["nombre"].insert(0, datos[1])
 
        self.entries["apellido"].delete(0, tk.END)
        self.entries["apellido"].insert(0, datos[2])
 
        self.entries["tipo_vehiculo"].set(datos[3] or "")
 
        self.entries["placa"].delete(0, tk.END)
        self.entries["placa"].insert(0, datos[4])
 
        self.estado_var.set(datos[5] or "disponible")
 
    def _limpiar_formulario(self):
        
        super()._limpiar_formulario()
        self.estado_var.set("disponible")
 
    def _obtener_datos_formulario(self):
        
        nombre = self.entries["nombre"].get().strip()
        apellido = self.entries["apellido"].get().strip()
        vehiculo = self.entries["tipo_vehiculo"].get()
        placa = self.entries["placa"].get().strip().upper()
        estado = self.estado_var.get()
 
        if not nombre or not apellido:
            messagebox.showwarning("Validación", "Nombre y apellido obligatorios")
            return None
 
        if not placa:
            messagebox.showwarning("Validación", "La placa es obligatoria")
            return None
 
        return {
            "nombre": nombre,
            "apellido": apellido,
            "tipo_vehiculo": vehiculo,
            "placa": placa,
            "estado": estado
        }
 
    def _formatear_fila(self, registro):
        
        return (
            getattr(registro, "id_repartidor", ""),
            getattr(registro, "nombre", ""),
            getattr(registro, "apellido", ""),
            getattr(registro, "tipo_vehiculo", ""),
            getattr(registro, "placa", ""),
            getattr(registro, "estado", "")
        )
 