import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import os

def cargar_usuarios(archivo):
    usuarios = {}
    try:
        with open(archivo, "r") as f:
            for linea in f:
                usuario, contraseña = linea.strip().split(":")
                usuarios[usuario] = contraseña
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo de usuarios no encontrado.")
    return usuarios

def iniciar_sesion():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    if usuario in usuarios and usuarios[usuario] == contraseña:
        messagebox.showinfo("Inicio de sesión", "Ha ingresado correctamente")
        frame_login.pack_forget()
        frame_principal.pack(fill=tk.BOTH, expand=True)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def cargar_datos(archivo):
    try:
        if archivo.endswith(".csv"):
            df = pd.read_csv(archivo, encoding="utf-8", sep=None, engine='python')
        elif archivo.endswith(".xlsx"):
            df = pd.read_excel(archivo)
        else:
            raise ValueError("Formato de archivo no soportado")
        return df
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
        return None

def mostrar_resultado(df_resultado):
    for widget in frame_resultados.winfo_children():
        widget.destroy()
    
    tree_frame = tk.Frame(frame_resultados)
    tree_frame.pack(fill=tk.BOTH, expand=True)
    
    y_scroll = ttk.Scrollbar(tree_frame)
    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    
    x_scroll = ttk.Scrollbar(tree_frame, orient='horizontal')
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)
    
    tree = ttk.Treeview(tree_frame, yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
    tree.pack(fill=tk.BOTH, expand=True)
    
    y_scroll.config(command=tree.yview)
    x_scroll.config(command=tree.xview)
    
    tree["columns"] = list(df_resultado.columns)
    tree.column("#0", width=0, stretch=tk.NO)
    
    for col in df_resultado.columns:
        tree.heading(col, text=col, anchor=tk.W)
        col_width = max(
            df_resultado[col].astype(str).map(len).max() * 8,
            len(col) * 8
        )
        tree.column(col, width=min(col_width, 200), anchor=tk.W)
    
    for index, row in df_resultado.iterrows():
        tree.insert("", "end", values=list(row))

def consulta_casas_mas_grandes():
    resultado = df.nlargest(5, "sq__ft")[["street", "city", "sq__ft", "price"]]
    mostrar_resultado(resultado.rename(columns={
        "street": "Dirección",
        "city": "Ciudad",
        "sq__ft": "Pies Cuadrados",
        "price": "Precio"
    }))

def consulta_mejores_promedios():
    resultado = df.groupby("city")["price"].mean().nlargest(5).reset_index()
    mostrar_resultado(resultado.rename(columns={
        "city": "Ciudad",
        "price": "Precio Promedio"
    }))

def consulta_top_casas_por_ciudad():
    resultado = df.groupby("city").apply(lambda x: x.nlargest(3, "price")[["street", "price"]]).reset_index()
    mostrar_resultado(resultado.rename(columns={
        "city": "Ciudad",
        "street": "Dirección",
        "price": "Precio"
    }))

def consulta_top_habitaciones_por_ciudad():
    resultado = df.groupby("city").apply(lambda x: x.nlargest(3, "beds")[["street", "beds"]]).reset_index()
    mostrar_resultado(resultado.rename(columns={
        "city": "Ciudad",
        "street": "Dirección",
        "beds": "Habitaciones"
    }))

def consulta_top_banos_por_ciudad():
    resultado = df.groupby("city").apply(lambda x: x.nlargest(3, "baths")[["street", "baths"]]).reset_index()
    mostrar_resultado(resultado.rename(columns={
        "city": "Ciudad",
        "street": "Dirección",
        "baths": "Baños"
    }))

def consulta_precio_promedio_ciudad():
    mostrar_resultado(df.groupby("city")["price"].mean().reset_index().rename(columns={
        "city": "Ciudad",
        "price": "Precio Promedio"
    }))

def consulta_promedio_pies_cuadrados_ciudad():
    mostrar_resultado(df.groupby("city")["sq__ft"].mean().reset_index().rename(columns={
        "city": "Ciudad",
        "sq__ft": "Promedio Pies Cuadrados"
    }))

def consulta_casas_tipo_residencial():
    mostrar_resultado(df[df["type"] == "Residential"][["street", "city", "price"]].rename(columns={
        "street": "Dirección",
        "city": "Ciudad",
        "price": "Precio"
    }))

def consulta_propiedades_por_codigo_postal():
    mostrar_resultado(df["zip"].value_counts().reset_index().rename(columns={
        "index": "Código Postal",
        "zip": "Cantidad"
    }))

root = tk.Tk()
root.title("Sistema de Consultas de Bienes Raíces")
root.geometry("1200x800")

frame_login = tk.Frame(root)
frame_login.pack(pady=50)

label_usuario = tk.Label(frame_login, text="Usuario:", font=("Arial", 12))
label_usuario.grid(row=0, column=0, padx=5, pady=5)
entry_usuario = tk.Entry(frame_login, font=("Arial", 12))
entry_usuario.grid(row=0, column=1, padx=5, pady=5)

label_contraseña = tk.Label(frame_login, text="Contraseña:", font=("Arial", 12))
label_contraseña.grid(row=1, column=0, padx=5, pady=5)
entry_contraseña = tk.Entry(frame_login, show="*", font=("Arial", 12))
entry_contraseña.grid(row=1, column=1, padx=5, pady=5)

btn_login = tk.Button(frame_login, text="Iniciar sesión", command=iniciar_sesion, font=("Arial", 12))
btn_login.grid(row=2, columnspan=2, pady=10)

usuarios = cargar_usuarios("usuarios.txt")

df = cargar_datos("Sacramentorealestatetransactions.xlsx")

frame_principal = tk.Frame(root)

frame_botones = tk.Frame(frame_principal)
frame_botones.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

frame_resultados = tk.Frame(frame_principal)
frame_resultados.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

botones_consulta = [
    ("Top 5 ciudades con mejores promedios", consulta_mejores_promedios),
    ("Top 5 casas más grandes (área)", consulta_casas_mas_grandes),
    ("Top 3 casas más caras por ciudad", consulta_top_casas_por_ciudad),
    ("Top 3 casas con más habitaciones por ciudad", consulta_top_habitaciones_por_ciudad),
    ("Top 3 casas con más baños por ciudad", consulta_top_banos_por_ciudad),
    ("Precio promedio por ciudad", consulta_precio_promedio_ciudad),
    ("Promedio de pies cuadrados por ciudad", consulta_promedio_pies_cuadrados_ciudad),
    ("Casas de tipo residencial", consulta_casas_tipo_residencial),
    ("Propiedades por código postal", consulta_propiedades_por_codigo_postal),
]

for texto, comando in botones_consulta:
    btn = tk.Button(frame_botones, text=texto, command=comando, width=30, height=2, 
                   wraplength=200, font=("Arial", 10))
    btn.pack(pady=5, padx=5, anchor="w")

root.mainloop()
