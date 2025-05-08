import tkinter as tk
from tkinter import ttk, messagebox
from excel import todoslosnombres,obtenerDatos
from excel_su import obtenersuce

class FichaTrabajadorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ficha del Trabajador")
        self.geometry("800x600")
        
        
        self.trabajadores = todoslosnombres()
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('TLabel', font=('Arial', 10))
        
        # Inicializar la interfaz
        self.init_ui()
        
    def init_ui(self):
        # Parte superior - selección de trabajador
        frame_top = ttk.Frame(self)
        frame_top.pack(pady=10, fill=tk.X)
        
        ttk.Label(frame_top, text="Seleccionar Trabajador:").pack(side=tk.LEFT, padx=5)
        
        self.combo_trabajadores = ttk.Combobox(frame_top, values=self.trabajadores, width=40)
        self.combo_trabajadores.pack(side=tk.LEFT, padx=10)
        
        ttk.Button(frame_top, text="Cargar Datos", command=self.cargar_datos).pack(side=tk.LEFT, padx=5)
        
        # Tabs principales
        self.tab_control = ttk.Notebook(self)
        self.tab_control.pack(expand=1, fill='both', padx=10, pady=10)
        
        # Tab Información Personal
        self.tab_info = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_info, text="Información Personal")
        
        # Contenido de la pestaña de información personal
        info_frame = ttk.Frame(self.tab_info, padding=10)
        info_frame.pack(fill='both', expand=True)
        
        # Campos de información personal con grid para mejor organización
        ttk.Label(info_frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.txt_nombre = ttk.Entry(info_frame, width=30)
        self.txt_nombre.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(info_frame, text="RUT:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.txt_rut = ttk.Entry(info_frame, width=30)
        self.txt_rut.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(info_frame, text="Cargo:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.txt_cargo = ttk.Entry(info_frame, width=30)
        self.txt_cargo.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(info_frame, text="Departamento:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.txt_depto = ttk.Entry(info_frame, width=30)
        self.txt_depto.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(info_frame, text="Fecha Contratación:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.txt_fecha = ttk.Entry(info_frame, width=30)
        self.txt_fecha.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Tab Sucesión
        self.tab_sucesion = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_sucesion, text="Sucesión")
        
        # Contenido del tab sucesión
        sucesion_frame = ttk.Frame(self.tab_sucesion, padding=10)
        sucesion_frame.pack(fill='both', expand=True)
        
      
        label_row = ttk.Frame(sucesion_frame)
        label_row.pack(fill=tk.X, pady=5)
        ttk.Label(label_row, text="Cargo actual del empleado:").pack(side=tk.LEFT, padx=5)
        ttk.Label(label_row, text="Plan de sucesión del empleado:").pack(side=tk.LEFT, padx=202)


        # Frame para la lista y botones
        list_frame = ttk.Frame(sucesion_frame)
        list_frame.pack(fill='both', expand=True, pady=5)
        
        # Lista de sucesión
        self.list_cargoactual = tk.Listbox(list_frame, height=10)
        self.list_cargoactual.pack(side=tk.LEFT, fill='both', expand=True, padx=5)

        self.list_sucesion = tk.Listbox(list_frame, height=10)
        self.list_sucesion.pack(side=tk.LEFT, fill='both', expand=True, padx=5)
        
        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.list_sucesion.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.list_sucesion.config(yscrollcommand=scrollbar.set)
        
        # Botones de acción para sucesión
        btn_frame = ttk.Frame(sucesion_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(btn_frame, text="Agregar Sucesión", command=self.agregar_sucesion).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Eliminar Seleccionado", command=self.eliminar_sucesion).pack(side=tk.LEFT, padx=5)
        
        # Tab Planes de Desarrollo
        self.tab_desarrollo = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_desarrollo, text="Planes de Desarrollo")
        
        # Contenido del tab desarrollo
        desarrollo_frame = ttk.Frame(self.tab_desarrollo, padding=10)
        desarrollo_frame.pack(fill='both', expand=True)
        
        ttk.Label(desarrollo_frame, text="Planes de desarrollo:").pack(anchor=tk.W, pady=5)
        
        # Frame para la lista y botones
        list_dev_frame = ttk.Frame(desarrollo_frame)
        list_dev_frame.pack(fill='both', expand=True, pady=5)
        
        # Lista de desarrollo
        self.list_desarrollo = tk.Listbox(list_dev_frame, height=10)
        self.list_desarrollo.pack(side=tk.LEFT, fill='both', expand=True, padx=5)
        
        # Scrollbar para la lista
        scrollbar_dev = ttk.Scrollbar(list_dev_frame, orient="vertical", command=self.list_desarrollo.yview)
        scrollbar_dev.pack(side=tk.RIGHT, fill=tk.Y)
        self.list_desarrollo.config(yscrollcommand=scrollbar_dev.set)
        
        # Botones de acción para desarrollo
        btn_dev_frame = ttk.Frame(desarrollo_frame)
        btn_dev_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(btn_dev_frame, text="Agregar Plan", command=self.agregar_plan).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_dev_frame, text="Eliminar Seleccionado", command=self.eliminar_plan).pack(side=tk.LEFT, padx=5)
        
        # Botones de acción generales
        action_frame = ttk.Frame(self)
        action_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(action_frame, text="Guardar Cambios", command=self.guardar_cambios).pack(side=tk.RIGHT, padx=5)

    def cargar_datos(self):
        seleccionado = self.combo_trabajadores.get()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Selecciona un trabajador.")
            return
        
        datos = obtenerDatos(seleccionado)
        self.txt_nombre.delete(0, tk.END)
        self.txt_nombre.insert(0, datos[0])
        self.txt_rut.delete(0, tk.END)
        self.txt_rut.insert(0, datos[1])
        self.txt_cargo.delete(0, tk.END)
        self.txt_cargo.insert(0, datos[3])
        self.txt_depto.delete(0, tk.END)
        self.txt_depto.insert(0, datos[4])
        self.txt_fecha.delete(0, tk.END)
        self.txt_fecha.insert(0, datos[2])
            
          
        self.list_sucesion.delete(0, tk.END)
        suc = obtenersuce(datos[1])
        for sucesion in suc.get("sucesion", []):
            if sucesion == 4:
                self.list_sucesion.insert(tk.END, "SIN SUCESION")   
            else: 
                self.list_sucesion.insert(tk.END, sucesion)
        self.list_cargoactual.delete(0, tk.END)
        for cargo in suc.get("cargo_actual", []):
            if cargo == 4:
                self.list_cargoactual.insert(tk.END,datos[3])
            else:
                self.list_cargoactual.insert(tk.END, cargo)
        
            
        self.list_desarrollo.delete(0, tk.END)
        self.list_desarrollo.insert(tk.END, "Curso Liderazgo", "Mentoría Interna")
        

    def agregar_sucesion(self):
        
        nueva_sucesion = "Nueva Sucesión"
        self.list_sucesion.insert(tk.END, nueva_sucesion)

    def eliminar_sucesion(self):
        seleccion = self.list_sucesion.curselection()
        if seleccion:
            self.list_sucesion.delete(seleccion)
        else:
            messagebox.showinfo("Información", "Selecciona un elemento para eliminar")

    def agregar_plan(self):
        nuevo_plan = "Nuevo Plan de Desarrollo"
        self.list_desarrollo.insert(tk.END, nuevo_plan)

    def eliminar_plan(self):
        seleccion = self.list_desarrollo.curselection()
        if seleccion:
            self.list_desarrollo.delete(seleccion)
        else:
            messagebox.showinfo("Información", "Selecciona un elemento para eliminar")
            
    def guardar_cambios(self):
        
        messagebox.showinfo("Información", "Cambios guardados correctamente")

if __name__ == "__main__":
    app = FichaTrabajadorApp()
    app.mainloop()