import tkinter as tk

class EjercicioBase:
    def __init__(self, frame, regresar_callback):
        self.frame = frame
        self.regresar_callback = regresar_callback
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.frame, text=f"{self.__class__.__name__}").pack(pady=10)
        tk.Button(self.frame, text="Menu", command=self.regresar_callback).pack(pady=10)

# Ejercicios
class Ejercicio1(EjercicioBase):
    def create_widgets(self):
        super().create_widgets()
        tk.Label(self.frame, text="Evalúe el aumento que recibe un trabajador, sabiendo que se le aplica un aumento del 15% de su sueldo básico, si este es menor de $4000 y 8% en caso contrario").pack()
        tk.Label(self.frame, text="Ingrese sueldo:").pack()
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        tk.Button(self.frame, text="Calcular", command=self.calcular).pack()
        self.resultado = tk.Label(self.frame, text="")
        self.resultado.pack()
    
    def calcular(self):
        sueldo = float(self.entry.get())
        aumento = sueldo * 0.15 if sueldo < 4000 else sueldo * 0.08
        self.resultado.config(text=f"Nuevo sueldo: {sueldo + aumento}")

class Ejercicio2(EjercicioBase):
    def create_widgets(self):
        super().create_widgets()
        tk.Label(self.frame, text="En un parque de diversiones a las personas menores de 10 años se les hace un descuento del 25 % sobre el precio del juego que vale 50 soles. Cuanto debe pagar un niño y cuánto debe pagar una persona que no es niño.").pack() 
        tk.Label(self.frame, text="Ingrese edad:").pack()
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        tk.Button(self.frame, text="Calcular", command=self.calcular).pack()
        self.resultado = tk.Label(self.frame, text="")
        self.resultado.pack()
    
    def calcular(self):
        edad = int(self.entry.get())
        precio = 50 * 0.75 if edad < 10 else 50
        self.resultado.config(text=f"Monto a pagar: {precio} soles")

class Ejercicio3(EjercicioBase):
    def create_widgets(self):
        super().create_widgets()
        tk.Label(self.frame, text="Una tienda ofrece un descuento del 15 % sobre el total de la compra durante el mes de octubre. Dado un mes y un importe, calcular cuál es la cantidad que se debe cobrar al cliente.").pack()
        tk.Label(self.frame, text="Ingrese mes y monto:").pack()
        self.entry_mes = tk.Entry(self.frame)
        self.entry_mes.pack()
        self.entry_monto = tk.Entry(self.frame)
        self.entry_monto.pack()
        tk.Button(self.frame, text="Calcular", command=self.calcular).pack()
        self.resultado = tk.Label(self.frame, text="")
        self.resultado.pack()
    
    def calcular(self):
        mes = self.entry_mes.get().strip().lower()
        monto = float(self.entry_monto.get())
        descuento = 0.15 if mes == "octubre" else 0
        total = monto * (1 - descuento)
        self.resultado.config(text=f"Total a pagar: {total}")

class Ejercicio4(EjercicioBase):
    def create_widgets(self):
        super().create_widgets()
        tk.Label(self.frame, text="Escriba un algoritmo que lea del teclado un número entero y que compruebe si el número es menor que 10. Si no lo está, debe volver a leer el número repitiendo la operación hasta que el usuario escriba un valor correcto. Finalmente, debe escribir por pantalla el valor leído cuando este sea correcto.").pack(pady=5)
        tk.Label(self.frame, text="Ingrese un número menor que 10:").pack()
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        tk.Button(self.frame, text="Validar", command=self.validar).pack()
        self.resultado = tk.Label(self.frame, text="")
        self.resultado.pack()
    
    def validar(self):
        try:
            num = int(self.entry.get())
            if num < 10:
                self.resultado.config(text=f"Número válido ingresado: {num}")
            else:
                self.resultado.config(text="Número inválido. Ingrese un número menor que 10.")
        except ValueError:
            self.resultado.config(text="Entrada no válida. Ingrese un número entero.")

class Ejercicio5(EjercicioBase):
    def create_widgets(self):
        super().create_widgets()
        tk.Label(self.frame, text="Modifique el algoritmo del problema anterior para que, en vez de comprobar que el número sea menor que 10, compruebe que se encuentre en el rango (0, 20).").pack()
        tk.Label(self.frame, text="Ingrese un número en el rango (0, 20):").pack()
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        tk.Button(self.frame, text="Validar", command=self.validar).pack()
        self.resultado = tk.Label(self.frame, text="")
        self.resultado.pack()
    
    def validar(self):
        num = int(self.entry.get())
        if 0 <= num <= 20:
            self.resultado.config(text=f"Número válido: {num}")
        else:
            self.resultado.config(text="Número fuera de rango (0, 20)")

class Ejercicio6(EjercicioBase):
    def create_widgets(self):
        super().create_widgets()
        tk.Label(self.frame, text="Modifique el algoritmo del problema anterior para que cuente las veces que ha leído un número de teclado y escriba el resultado por pantalla.").pack()
        tk.Label(self.frame, text="Ingrese números (se detiene cuando ingrese 0):").pack()
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        tk.Button(self.frame, text="Ingresar", command=self.contar_intentos).pack()
        self.resultado = tk.Label(self.frame, text="")
        self.resultado.pack()
        self.contador = 0
    
    def contar_intentos(self):
        numero = int(self.entry.get())
        self.contador += 1
        if numero == 0:
            self.resultado.config(text=f"Se ingresaron {self.contador - 1} números.")
        else:
            self.resultado.config(text=f"Números leídos: {self.contador}")

class Ejercicio7(EjercicioBase):
    def create_widgets(self):
        super().create_widgets()
        tk.Label(self.frame, text="Escriba un algoritmo que calcule e imprima la suma de los n primeros números enteros positivos. El valor de n debe leerse del teclado y ser ingresado por el usuario.").pack()
        tk.Label(self.frame, text="Ingrese un número n para calcular la suma de los primeros n números:").pack()
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        tk.Button(self.frame, text="Calcular", command=self.calcular_suma).pack()
        self.resultado = tk.Label(self.frame, text="")
        self.resultado.pack()
    
    def calcular_suma(self):
        n = int(self.entry.get())
        suma = sum(range(1, n + 1))
        self.resultado.config(text=f"La suma de los primeros {n} números es: {suma}")

class Ejercicio8(EjercicioBase):
    def create_widgets(self):
        super().create_widgets()
        tk.Label(self.frame, text="Escriba un algoritmo que sume los números ingresados por el usuario hasta que el usuario ingrese el número 0 (detener las preguntas ante este escenario).").pack()
        tk.Label(self.frame, text="Ingrese números para sumar (ingrese 0 para terminar):").pack()
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        tk.Button(self.frame, text="Sumar", command=self.sumar_numeros).pack()
        self.resultado = tk.Label(self.frame, text="")
        self.resultado.pack()
        self.suma_total = 0
    
    def sumar_numeros(self):
        numero = int(self.entry.get())
        if numero == 0:
            self.resultado.config(text=f"Suma total: {self.suma_total}")
        else:
            self.suma_total += numero
            self.resultado.config(text=f"Suma en curso: {self.suma_total}")

class Ejercicio9(EjercicioBase):
    def create_widgets(self):
        super().create_widgets()
        tk.Label(self.frame, text="Escriba un algoritmo que sume los números ingresados por el usuario y cuando la suma sea superior a 100 deje de pedir números y muestre el total.").pack()
        tk.Label(self.frame, text="Ingrese números para sumar (se detiene cuando la suma sea mayor a 100):").pack()
        self.entry = tk.Entry(self.frame)
        self.entry.pack()
        tk.Button(self.frame, text="Sumar", command=self.sumar_hasta_100).pack()
        self.resultado = tk.Label(self.frame, text="")
        self.resultado.pack()
        self.suma_total = 0
    
    def sumar_hasta_100(self):
        numero = int(self.entry.get())
        self.suma_total += numero
        if self.suma_total > 100:
            self.resultado.config(text=f"Suma total superior a 100: {self.suma_total}")
        else:
            self.resultado.config(text=f"Suma en curso: {self.suma_total}")

class Ejercicio10(EjercicioBase):
    def create_widgets(self):
        super().create_widgets()
        tk.Label(self.frame, text="Se desea tener un algoritmo que permita mostrar el nombre, el monto por trabajar las horas normales, el monto por trabajar las horas extras, la bonificación total por los hijos (por cada hijo se le da 0. 5) y finalmente el pago total (es la suma del monto por pago de las horas normales, monto por pago de las horas extras y la bonificación total por los hijos).").pack()
        tk.Label(self.frame, text="Considere que el pago por hora extra es 50% más del pago por hora normal.").pack()
        tk.Label(self.frame, text="Ingrese nombre, horas normales, horas extras y cantidad de hijos:").pack()
        self.entry_nombre = tk.Entry(self.frame)
        self.entry_nombre.pack()
        self.entry_horas_normales = tk.Entry(self.frame)
        self.entry_horas_normales.pack()
        self.entry_horas_extras = tk.Entry(self.frame)
        self.entry_horas_extras.pack()
        self.entry_hijos = tk.Entry(self.frame)
        self.entry_hijos.pack()
        tk.Button(self.frame, text="Calcular pago total", command=self.calcular_pago).pack()
        self.resultado = tk.Label(self.frame, text="")
        self.resultado.pack()
    
    def calcular_pago(self):
        nombre = self.entry_nombre.get()
        horas_normales = int(self.entry_horas_normales.get())
        horas_extras = int(self.entry_horas_extras.get())
        hijos = int(self.entry_hijos.get())
        
        pago_hora_normal = 10
        pago_hora_extra = pago_hora_normal * 1.5
        bonificacion_hijos = hijos * 0.5
        
        pago_total = (horas_normales * pago_hora_normal) + (horas_extras * pago_hora_extra) + bonificacion_hijos
        self.resultado.config(text=f"Nombre: {nombre}\nPago total: {pago_total}\nBonificación por hijos: {bonificacion_hijos}")

