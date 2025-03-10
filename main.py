from ejercicios_OGL  import EjercicioBase, Ejercicio1, Ejercicio2, Ejercicio3, Ejercicio4, Ejercicio5, Ejercicio6, Ejercicio7, Ejercicio8, Ejercicio9, Ejercicio10
import tkinter as tk

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú de Ejercicios")
        self.frame = None
        self.mostrar_menu()
    
    def mostrar_menu(self):
        if self.frame:
            self.frame.destroy()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        tk.Label(self.frame, text="Olvera Gil Leonel").pack(pady=10)
        tk.Label(self.frame, text="6IV6").pack(pady=10)
        tk.Label(self.frame, text="Ejercicios de Python").pack(pady=10)
        for i in range(1, 11):
            tk.Button(self.frame, text=f"Ejercicio_{i}", command=lambda i=i: self.mostrar_ejercicio(globals()[f"Ejercicio{i}"])).pack(pady=5)
    
    def mostrar_ejercicio(self, clase):
        if self.frame:
            self.frame.destroy()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        clase(self.frame, self.mostrar_menu)

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPrincipal(root)
    root.mainloop()