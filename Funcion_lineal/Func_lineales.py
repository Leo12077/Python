import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FuncionLinealApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Funciones Lineales")
        self.root.geometry("1000x800")

        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True)

        left_frame = tk.Frame(main_frame, padx=20, pady=20)
        left_frame.pack(side="left", fill="both", expand=True)

        inner_left_frame = tk.Frame(left_frame)
        inner_left_frame.pack(expand=True)
        
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side="right", fill="both", expand=True)

        ttk.Label(inner_left_frame, text="Pendiente (m):", font=("Arial", 15)).pack(pady=5, anchor="center")
        self.entry_m = ttk.Entry(inner_left_frame, width=20)
        self.entry_m.pack(pady=5)

        ttk.Label(inner_left_frame, text="Término independiente (b):", font=("Arial", 15)).pack(pady=5, anchor="center")
        self.entry_b = ttk.Entry(inner_left_frame, width=20)
        self.entry_b.pack(pady=5)

        self.generar_btn = ttk.Button(inner_left_frame, text="Graficar función", command=self.generar_funcion)
        self.generar_btn.pack(pady=10)

        self.funcion_label = ttk.Label(inner_left_frame, text="", font=("Arial", 20))
        self.funcion_label.pack(pady=20)
        
        # Área de gráfica en el lado derecho
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=right_frame)
        self.canvas.get_tk_widget().pack(padx=10, pady=10, fill="both", expand=True)

    def generar_funcion(self):
        try:
            m = float(self.entry_m.get())
            b = float(self.entry_b.get())

            signo = "+" if b >= 0 else "-"
            self.funcion_label.config(text=f"f(x) = {m}x {signo} {abs(b)}")

            x_vals = list(range(-10, 11))
            y_vals = [m * x + b for x in x_vals]

            self.ax.clear()
            self.ax.plot(x_vals, y_vals, label=f"f(x) = {m}x {signo} {abs(b)}", color='red')
            self.ax.axhline(0, color='black', linewidth=1)
            self.ax.axvline(0, color='black', linewidth=1)
            self.ax.grid(True)
            self.ax.legend()
            self.canvas.draw()

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para m y b.")

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = FuncionLinealApp(root)
    root.mainloop()
