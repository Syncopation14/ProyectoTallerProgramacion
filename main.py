import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from excel import todoslosnombres,obtenerDatos
from excel_su import obtenersuce

class FichaTrabajadorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ficha del Trabajador")
        self.geometry("800x600")

        try:
            # Cargar y redimensionar imagen de fondo
            self.image = Image.open(r"C:\Users\claus\Downloads\cod_claudio\cod_claudio\fondo.jpg")
            self.image = self.image.resize((800, 600), Image.Resampling.LANCZOS)
            self.img_tk = ImageTk.PhotoImage(self.image)

            # Canvas para fondo
            self.canvas = tk.Canvas(self, width=800, height=600)
            self.canvas.pack(fill="both", expand=True)
            self.canvas.create_image(400, 300, image=self.img_tk, anchor="center")  # Centrar imagen

            # Frame contenedor principal sobre canvas (transparente)
            self.main_frame = tk.Frame(self.canvas, bg= "#f0f0f0", bd=0)
            self.canvas.create_window(400, 300, window=self.main_frame, anchor="center", width=780, height=580)

        except Exception as e:
            print(f"Error cargando imagen: {e}")
            # Si falla, crear sin imagen de fondo
            self.main_frame = tk.Frame(self)
            self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.trabajadores = todoslosnombres()

        # Configurar estilo
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('TLabel', font=('Arial', 10))

        # Inicializar la interfaz
        self.init_ui()

    def init_ui(self):
        frame_top = ttk.Frame(self.main_frame)
        frame_top.pack(pady=10, fill=tk.X)

        ttk.Label(frame_top, text="Seleccionar Trabajador:").pack(side=tk.LEFT, padx=5)
        self.combo_trabajadores = ttk.Combobox(frame_top, values=self.trabajadores, width=40)
        self.combo_trabajadores.pack(side=tk.LEFT, padx=10)
        ttk.Button(frame_top, text="Cargar Datos", command=self.cargar_datos).pack(side=tk.LEFT, padx=5)

        self.tab_control = ttk.Notebook(self.main_frame)
        self.tab_control.pack(expand=1, fill='both', padx=10, pady=10)

        # TAB INFORMACIÓN PERSONAL
        self.tab_info = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_info, text="Información Personal")
        info_frame = ttk.Frame(self.tab_info, padding=10)
        info_frame.pack(fill='both', expand=True)

        labels = ["Nombre:", "RUT:", "Cargo:", "Departamento:", "Fecha Contratación:"]
        self.entries = []
        for i, label in enumerate(labels):
            ttk.Label(info_frame, text=label).grid(row=i, column=0, sticky=tk.W, pady=5)
            entry = ttk.Entry(info_frame, width=30)
            entry.grid(row=i, column=1, sticky=tk.W, padx=5, pady=5)
            self.entries.append(entry)

        self.txt_nombre, self.txt_rut, self.txt_cargo, self.txt_depto, self.txt_fecha = self.entries

        # TAB SUCESIÓN
        self.tab_sucesion = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_sucesion, text="Sucesión")
        sucesion_frame = ttk.Frame(self.tab_sucesion, padding=10)
        sucesion_frame.pack(fill='both', expand=True)

        label_row = ttk.Frame(sucesion_frame)
        label_row.pack(fill=tk.X, pady=5)
        ttk.Label(label_row, text="Cargo actual del empleado:").pack(side=tk.LEFT, padx=5)
        ttk.Label(label_row, text="Plan de sucesión del empleado:").pack(side=tk.LEFT, padx=202)

        list_frame = ttk.Frame(sucesion_frame)
        list_frame.pack(fill='both', expand=True, pady=5)

        self.list_cargoactual = tk.Listbox(list_frame, height=10)
        self.list_cargoactual.pack(side=tk.LEFT, fill='both', expand=True, padx=5)
        self.list_sucesion = tk.Listbox(list_frame, height=10)
        self.list_sucesion.pack(side=tk.LEFT, fill='both', expand=True, padx=5)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.list_sucesion.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.list_sucesion.config(yscrollcommand=scrollbar.set)

        btn_frame = ttk.Frame(sucesion_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        ttk.Button(btn_frame, text="Agregar Sucesión", command=self.agregar_sucesion).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Eliminar Seleccionado", command=self.eliminar_sucesion).pack(side=tk.LEFT, padx=5)

        # TAB DESARROLLO
        self.tab_desarrollo = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_desarrollo, text="Planes de Desarrollo")
        desarrollo_frame = ttk.Frame(self.tab_desarrollo, padding=10)
        desarrollo_frame.pack(fill='both', expand=True)
        ttk.Label(desarrollo_frame, text="Planes de desarrollo:").pack(anchor=tk.W, pady=5)

        list_dev_frame = ttk.Frame(desarrollo_frame)
        list_dev_frame.pack(fill='both', expand=True, pady=5)
        self.list_desarrollo = tk.Listbox(list_dev_frame, height=10)
        self.list_desarrollo.pack(side=tk.LEFT, fill='both', expand=True, padx=5)

        scrollbar_dev = ttk.Scrollbar(list_dev_frame, orient="vertical", command=self.list_desarrollo.yview)
        scrollbar_dev.pack(side=tk.RIGHT, fill=tk.Y)
        self.list_desarrollo.config(yscrollcommand=scrollbar_dev.set)

        btn_dev_frame = ttk.Frame(desarrollo_frame)
        btn_dev_frame.pack(fill=tk.X, pady=5)
        ttk.Button(btn_dev_frame, text="Agregar Plan", command=self.agregar_plan).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_dev_frame, text="Eliminar Seleccionado", command=self.eliminar_plan).pack(side=tk.LEFT, padx=5)

        action_frame = ttk.Frame(self.main_frame)
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
            self.list_sucesion.insert(tk.END, "SIN SUCESION" if sucesion == 4 else sucesion)
        self.list_cargoactual.delete(0, tk.END)
        for cargo in suc.get("cargo_actual", []):
            self.list_cargoactual.insert(tk.END, datos[3] if cargo == 4 else cargo)

        self.list_desarrollo.delete(0, tk.END)
        self.list_desarrollo.insert(tk.END, "Curso Liderazgo", "Mentoría Interna")

    def agregar_sucesion(self):
        self.list_sucesion.insert(tk.END, "Nueva Sucesión")

    def eliminar_sucesion(self):
        seleccion = self.list_sucesion.curselection()
        if seleccion:
            self.list_sucesion.delete(seleccion)
        else:
            messagebox.showinfo("Información", "Selecciona un elemento para eliminar")

    def agregar_plan(self):
        self.list_desarrollo.insert(tk.END, "Nuevo Plan de Desarrollo")

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
