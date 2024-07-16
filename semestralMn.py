import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO
from PIL import Image

def mostrarSeccionPresentacion():
    textResultados.delete(1.0, tk.END)
    textResultados.insert(tk.END, "=" * 60 + "\n")
    textResultados.insert(tk.END, "{:^60}".format("Universidad Tecnológica de Panamá") + "\n")
    textResultados.insert(tk.END, "{:^60}".format("Facultad de Ingeniería de Sistemas Computacionales") + "\n")
    textResultados.insert(tk.END, "{:^60}".format("Métodos Numéricos para Ingenieros") + "\n")
    textResultados.insert(tk.END, "{:^60}".format("Proyecto Semestral") + "\n")
    textResultados.insert(tk.END, "{:^60}".format("Profesor: Henry Archibold") + "\n")
    textResultados.insert(tk.END, "{:^60}".format("Integrantes del equipo:") + "\n")
    textResultados.insert(tk.END, "{:^60}".format("- Wilfredo Cano 8-1003-721") + "\n")
    textResultados.insert(tk.END, "{:^60}".format("- Daniel Maestre 8-1005-1509") + "\n")
    textResultados.insert(tk.END, "{:^60}".format("- Jeremiah Kurmaty 8-1004-172") + "\n")
    textResultados.insert(tk.END, "{:^60}".format("- Allan Vega 8-1001-2089") + "\n")
    textResultados.insert(tk.END, "{:^60}".format("Salón: 1SF131") + "\n")
    textResultados.insert(tk.END, "{:^60}".format("Año 2024") + "\n")
    textResultados.insert(tk.END, "=" * 60 + "\n")

def f(x, y, ecuacion):
    return eval(ecuacion)

def eulerEstandar(x0, y0, h, xn, ecuacion):
    valorX = [x0]
    valorY = [y0]

    while valorX[-1] < xn:
        xI = round(valorX[-1],3)
        yI = valorY[-1]
        ySiguiente = yI + h * f(xI, yI, ecuacion)
        valorX.append(xI + h)
        valorY.append(ySiguiente)

    return valorX, valorY

def eulerModificado(x0, y0, h, xn, ecuacion):
    valorX = [x0]
    valorY = [y0]

    while valorX[-1] < xn:
        xI = round(valorX[-1],3)
        yI = valorY[-1]
        predictorY = yI + h * f(xI, yI, ecuacion)
        correctorY = yI + h/2 * (f(xI, yI, ecuacion) + f(xI + h, predictorY, ecuacion))
        valorX.append(xI + h)
        valorY.append(correctorY)

    return valorX, valorY

def rungeKutta1erOrden(x0, y0, h, xn, ecuacion):
    return eulerEstandar(x0, y0, h, xn, ecuacion)

def rungeKutta2doOrden(x0, y0, h, xn, ecuacion):
    valorX = [x0]
    valorY = [y0]

    while valorX[-1] < xn:
        xI = round(valorX[-1],3)
        yI = valorY[-1]
        k1 = h * f(xI, yI, ecuacion)
        k2 = h * f(xI + h, yI + k1, ecuacion)
        ySiguiente = yI + 0.5 * (k1 + k2)
        valorX.append(xI + h)
        valorY.append(ySiguiente)

    return valorX, valorY

def rungeKutta4toOrden(x0, y0, h, xn, ecuacion):
    valorX = [x0]
    valorY = [y0]

    while valorX[-1] < xn:
        xI = round(valorX[-1],3)
        yI = valorY[-1]
        k1 = h * f(xI, yI, ecuacion)
        k2 = h * f(xI + 0.5 * h, yI + 0.5 * k1, ecuacion)
        k3 = h * f(xI + 0.5 * h, yI + 0.5 * k2, ecuacion)
        k4 = h * f(xI + h, yI + k3, ecuacion)
        ySiguiente = yI + (k1 + 2*k2 + 2*k3 + k4) / 6
        valorX.append(xI + h)
        valorY.append(ySiguiente)

    return valorX, valorY

def mostrarGrafica(valorX, valorY, metodo):
    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(111)
    ax.plot(valorX, valorY, marker='o', linestyle='-', color='b', label='Solución numérica')
    ax.set_title(f'Solución usando el método de {metodo}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True)
    return fig

def calcular():
    metodo = metodoSeleccionado.get()
    ecuacion = entradaEcuacion.get()
    try:
        x0 = float(entradaX0.get())
        y0 = float(entradaY0.get())
        h = float(entradaH.get())
        xn = float(entradaXn.get())
    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingrese valores numéricos válidos.")
        return

    if metodo == "Euler estándar":
        valorX, valorY = eulerEstandar(x0, y0, h, xn, ecuacion)
    elif metodo == "Euler modificado":
        valorX, valorY = eulerModificado(x0, y0, h, xn, ecuacion)
    elif metodo == "Runge-Kutta 1er Orden":
        valorX, valorY = rungeKutta1erOrden(x0, y0, h, xn, ecuacion)
    elif metodo == "Runge-Kutta 2do Orden":
        valorX, valorY = rungeKutta2doOrden(x0, y0, h, xn, ecuacion)
    elif metodo == "Runge-Kutta 4to Orden":
        valorX, valorY = rungeKutta4toOrden(x0, y0, h, xn, ecuacion)
    else:
        messagebox.showerror("Método no seleccionado", "Por favor, seleccione un método válido.")
        return

    mostrarResultados(valorX, valorY, metodo)
    fig = mostrarGrafica(valorX, valorY, metodo)

    for widget in frameGrafica.winfo_children():
        widget.destroy()

    canvasGrafica = FigureCanvasTkAgg(fig, master=frameGrafica)
    canvasGrafica.draw()
    canvasGrafica.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Convertir la figura en una imagen en memoria
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    global img
    img = Image.open(buf)
    img = img.convert('RGB')

def mostrarResultados(valorX, valorY, metodo):
    textResultados.delete(1.0, tk.END)
    textResultados.insert(tk.END, f"Resultados usando el método de {metodo}:\n")
    textResultados.insert(tk.END, f'''Ecuación diferencial: dy/dx = {entradaEcuacion.get()}\n''')
    textResultados.insert(tk.END, f"{'Iteración':<10} {'x':<10} {'y calculado':<15}\n")
    for i, (x, y) in enumerate(zip(valorX, valorY)):
        textResultados.insert(tk.END, f"{i:<10} {x:.2f} {y:.6f}\n")
    finalY = valorY[-1]
    textResultados.insert(tk.END, f"\nEl valor de y({valorX[-1]:.2f}) calculado con el método de {metodo} es: {finalY:.6f}")

def descargarPDF():
    c = canvas.Canvas("resultados.pdf", pagesize=letter)
    text = textResultados.get(1.0, tk.END)
    lines = text.split('\n')
    y = 750
    for line in lines:
        c.drawString(30, y, line)
        y -= 15
        if y < 40:
            c.showPage()
            y = 750

    # Convertir la imagen de PIL a formato que reportlab pueda usar
    buf = BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    # Usar ImageReader para convertir el objeto BytesIO
    image_reader = ImageReader(buf)
    c.drawImage(image_reader, 30, y-220, width=300, height=200)  # Ajusta las dimensiones y posición de la gráfica
    c.save()
    messagebox.showinfo("Descargar PDF", "El archivo PDF se ha guardado como 'resultados.pdf'.")

def limpiarResultados():
    textResultados.delete(1.0, tk.END)
    for widget in frameGrafica.winfo_children():
        widget.destroy()

def on_enter(event, button, color):
    button['background'] = color

def on_leave(event, button, color):
    button['background'] = color

root = tk.Tk()
root.title("Solución de Ecuaciones Diferenciales")

metodoSeleccionado = tk.StringVar()
metodoSeleccionado.set("Seleccione un método")

etiquetaTitulo = ttk.Label(root, text="Solución de Ecuaciones Diferenciales Ordinarias", font=("Helvetica", 16))
etiquetaMetodo = ttk.Label(root, text="Seleccione el método:")
menuMetodo = ttk.OptionMenu(root, metodoSeleccionado, "Seleccione un método", "Euler estándar", "Euler modificado", "Runge-Kutta 1er Orden", "Runge-Kutta 2do Orden", "Runge-Kutta 4to Orden")

etiquetaEcuacion = ttk.Label(root, text="Ingrese la ecuación diferencial (en términos de x e y separados por *):")
entradaEcuacion = ttk.Entry(root, width=30)

etiquetaX0 = ttk.Label(root, text="Valor inicial de x (x0):")
entradaX0 = ttk.Entry(root, width=10)

etiquetaY0 = ttk.Label(root, text=f"Valor inicial de y(x0):")
entradaY0 = ttk.Entry(root, width=10)

etiquetaH = ttk.Label(root, text="Tamaño del paso (h):")
entradaH = ttk.Entry(root, width=10)

etiquetaXn = ttk.Label(root, text="Valor final de x (xn):")
entradaXn = ttk.Entry(root, width=10)

botonCalcular = tk.Button(root, text="Calcular", command=calcular, bg='green')
botonPDF = tk.Button(root, text="Descargar PDF", command=descargarPDF, bg='blue')
botonPresentacion = tk.Button(root, text="Ver Portada", command=mostrarSeccionPresentacion, bg='purple')
botonLimpiar = tk.Button(root, text="Limpiar", command=limpiarResultados, bg='orange')
botonSalir = tk.Button(root, text="Salir", command=root.destroy, bg='red')

botonCalcular.bind("<Enter>", lambda event, b=botonCalcular: on_enter(event, b, 'lightgreen'))
botonCalcular.bind("<Leave>", lambda event, b=botonCalcular: on_leave(event, b, 'green'))

botonPDF.bind("<Enter>", lambda event, b=botonPDF: on_enter(event, b, 'lightblue'))
botonPDF.bind("<Leave>", lambda event, b=botonPDF: on_leave(event, b, 'blue'))

botonPresentacion.bind("<Enter>", lambda event, b=botonPresentacion: on_enter(event, b, 'plum'))
botonPresentacion.bind("<Leave>", lambda event, b=botonPresentacion: on_leave(event, b, 'purple'))

botonLimpiar.bind("<Enter>", lambda event, b=botonLimpiar: on_enter(event, b, 'lightyellow'))
botonLimpiar.bind("<Leave>", lambda event, b=botonLimpiar: on_leave(event, b, 'orange'))

botonSalir.bind("<Enter>", lambda event, b=botonSalir: on_enter(event, b, 'lightcoral'))
botonSalir.bind("<Leave>", lambda event, b=botonSalir: on_leave(event, b, 'red'))

# Creación del scrollbar y el widget de texto
frameResultados = ttk.Frame(root)
scrollbarResultados = ttk.Scrollbar(frameResultados)
textResultados = tk.Text(frameResultados, width=60, height=12, wrap='word', yscrollcommand=scrollbarResultados.set)
scrollbarResultados.config(command=textResultados.yview)

frameGrafica = ttk.Frame(root, width=500, height=250)  # Ajustar tamaño del frame de la gráfica

etiquetaTitulo.grid(column=0, row=0, columnspan=4, pady=10)
etiquetaMetodo.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
menuMetodo.grid(column=1, row=1, padx=5, pady=5, columnspan=3)

etiquetaEcuacion.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
entradaEcuacion.grid(column=1, row=2, padx=5, pady=5, columnspan=3)

etiquetaX0.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
entradaX0.grid(column=1, row=3, padx=5, pady=5, columnspan=3)

etiquetaY0.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)
entradaY0.grid(column=1, row=4, padx=5, pady=5, columnspan=3)

etiquetaH.grid(column=0, row=5, sticky=tk.E, padx=5, pady=5)
entradaH.grid(column=1, row=5, padx=5, pady=5, columnspan=3)

etiquetaXn.grid(column=0, row=6, sticky=tk.E, padx=5, pady=5)
entradaXn.grid(column=1, row=6, padx=5, pady=5, columnspan=3)

botonCalcular.grid(column=0, row=7, pady=10)
botonPDF.grid(column=1, row=7, pady=10)
botonPresentacion.grid(column=2, row=7, pady=10)
botonLimpiar.grid(column=3, row=7, pady=10)
botonSalir.grid(column=4, row=7, pady=10)

# Posicionamiento del frame de resultados y scrollbar
frameResultados.grid(column=0, row=8, columnspan=5, padx=10, pady=10, sticky='nsew')
scrollbarResultados.pack(side=tk.RIGHT, fill=tk.Y)
textResultados.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frameGrafica.grid(column=0, row=9, columnspan=5, padx=10, pady=10, sticky='nsew')  # Ajustar el sticky para expandir el frame
frameGrafica.pack_propagate(False)  # Prevenir que el frame cambie de tamaño

root.mainloop()
