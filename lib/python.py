
import tkinter as tk
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects
import numpy as np
from colorama import init, Fore, Back, Style
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import PhotoImage
import os
import sys
import io
from tkinter import filedialog
import pandas as pd
import datetime
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from tkinter import *
import time




# Guardar la salida estándar actual
original_stdout = sys.stdout
sys.stdout = io.StringIO()
from pygame import mixer
sys.stdout = original_stdout










############################################################FUNCIONES######################################################################

#CALCULO DE PRESION DE SATURACION
def calcular_presion():
    try:
        # Obtener los valores ingresados por el usuario
        A = float(VA.get())
        B = float(VB.get())
        C = float(VC.get())
        T = float(VT.get())

        A2 = float(VA2.get())
        B2 = float(VB2.get())
        C2 = float(VC2.get())
       
        # Calcular la presión de saturación 1
        P_saturacion1 = np.exp(A - (B / (T + C)))

        # Calcular la presión de saturación 2
        P_saturacion2 = np.exp(A2 - (B2 / (T + C2)))

        
        # Calcular las presiones para cada composición de mezcla
        X_especies1 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        X_especies2 = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
        P = [round(X1 * P_saturacion1 + X2 * P_saturacion2,3) for X1, X2 in zip(X_especies1, X_especies2)]
        Y1 = [round(X1*P_saturacion1/Pi, 3) for X1, Pi in zip(X_especies1, P)]
        
        # Limpiar tabla antes de insertar nuevos valores 
        tabla.delete(*tabla.get_children())

        # Insertar valores en la tabla
        for i in range(len(X_especies1)):
            tabla.insert("", tk.END, values=(X_especies1[i], X_especies2[i], Y1[i], P[i]))

        # Llamar a la función para graficar
        fig = graficar_funcion(X_especies1, P, Y1, P)

        # Crear un lienzo de Tkinter que contiene la figura
        canvas = FigureCanvasTkAgg(fig, master=ventana)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(relx=1204/1660, rely=374/900, width=390, height=390)

        # Configurar la altura de la tabla
        tabla_height = len(X_especies1) # Se agrega 1 para incluir la última fila
        tabla.config(height=tabla_height)
        
        resultado1.config(text=f"La presión de saturación del componente 1 es: {round(P_saturacion1,3)} kPa", fg="GREEN", bg ='white')
        resultado2.config(text=f"La presión de saturación del componente 2 es: {round(P_saturacion2,3)} kPa", fg="GREEN", bg = 'white')
        
        with open("_internal/_log.txt", "a") as archivo:
            hora = datetime.datetime.now().strftime("%H:%M:%S")
            archivo.write(hora)
            archivo.write(f"\n La presion de saturacion de la sustancia 1 es {P_saturacion1} \n")
            archivo.write(f"\n La presion de saturacion de la sustancia 2 es {P_saturacion2} \n")
            for i in range(0,11,1):
                archivo.write(f"\n Las presiones de saturacion de la solucion son: {P[i]} \n")
            for i in range(0,11,1):
                archivo.write(f"\n Fracciones de vapor Y1 para X1 = {X_especies1[i]} es: {Y1[i]} \n")



    except ValueError:
        resultado1.config(text="Error: Por favor ingrese números válidos", fg="RED")
        resultado2.config(text="Error: Por favor ingrese números válidos", fg="RED")

#GUARDAR GRAFICA
def GuardarGrafica():

        # Obtener los valores ingresados por el usuario
        A = float(VA.get())
        B = float(VB.get())
        C = float(VC.get())
        T = float(VT.get())

        A2 = float(VA2.get())
        B2 = float(VB2.get())
        C2 = float(VC2.get())
       
        # Calcular la presión de saturación 1
        P_saturacion1 = np.exp(A - (B / (T + C)))

        # Calcular la presión de saturación 2
        P_saturacion2 = np.exp(A2 - (B2 / (T + C2)))

        
        # Calcular las presiones para cada composición de mezcla
        X_especies1 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        X_especies2 = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
        P = [round(X1 * P_saturacion1 + X2 * P_saturacion2,3) for X1, X2 in zip(X_especies1, X_especies2)]
        Y1 = [round(X1*P_saturacion1/Pi, 3) for X1, Pi in zip(X_especies1, P)]
        
    
        # Llamar a la función para graficar
        fig = graficar_funcion(X_especies1, P, Y1, P)

        fig = Figure(figsize=(4, 4), dpi=100)
        plot = fig.add_subplot(1, 1, 1)



        plot.plot(X_especies1, P, label = 'x1')
        plot.plot(Y1, P, label = 'y1')
        plot.grid(True)

        # Configurar etiquetas de los ejes
        plot.set_xlabel('X1, Y1', fontsize = 10, font ='hooge 05_53' )
        plot.set_ylabel('P(kPa)', fontsize = 10, font = 'hooge 05_53')
        
    
        

        # Configurar el estilo de la línea y el marco 
        plot.spines['top'].set_visible(True)
        plot.spines['right'].set_visible(True)
        plot.spines['bottom'].set_visible(True)
        plot.spines['left'].set_visible(True)
        plot.spines['top'].set_linewidth(3)
        plot.spines['right'].set_linewidth(3)
        plot.spines['bottom'].set_linewidth(3)
        plot.spines['left'].set_linewidth(3)
        for spine in plot.spines.values():
            spine.set_edgecolor('#FFEAC7')  # Cambiar el color del borde

        # Guardar la figura en la resolución máxima
        canvas = FigureCanvas(fig)
        plot.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))

        plot.legend(fontsize=10)  # Tamaño de la fuente para la leyenda

        directorio = filedialog.askdirectory()
        if directorio:
            filename = f"{directorio}/grafica_{datetime.datetime.now():%Y%m%d_%H%M%S}.png"
            canvas.print_figure(filename, dpi=800, bbox_inches='tight')
            print(f"Gráfica guardada en: {filename}")

#Grafica
def graficar_funcion(x1, y1, x2, y2):

    fig = Figure(figsize=(4, 4), dpi=80)
    plot = fig.add_subplot(1, 1, 1)
    plot.plot(x1, y1, label = 'x1')
    plot.plot(x2, y2, label = 'y1')
    plot.grid(True)

    # Configurar etiquetas de los ejes
    plot.set_xlabel('X1, Y1', fontsize = 10, font ='hooge 05_53' )
    plot.set_ylabel('P(kPa)', fontsize = 10, font = 'hooge 05_53')
    
   

    # Configurar el estilo de la línea y el marco 
    plot.spines['top'].set_visible(True)
    plot.spines['right'].set_visible(True)
    plot.spines['bottom'].set_visible(True)
    plot.spines['left'].set_visible(True)
    plot.spines['top'].set_linewidth(3)
    plot.spines['right'].set_linewidth(3)
    plot.spines['bottom'].set_linewidth(3)
    plot.spines['left'].set_linewidth(3)
    for spine in plot.spines.values():
        spine.set_edgecolor('#FFEAC7')  # Cambiar el color del borde



    plot.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))

    plot.legend(fontsize=10)  # Tamaño de la fuente para la leyenda


    return fig

#LIMPIAR VALORES
def Limpiarvalores():
    VA.delete(0, tk.END)  # Limpiar el contenido de los Entry
    VB.delete(0, tk.END)
    VC.delete(0, tk.END)
    VT.delete(0, tk.END)
    VA2.delete(0, tk.END)
    VB2.delete(0, tk.END)
    VC2.delete(0, tk.END)

    #Limpiar grafica
    for widget in ventana.winfo_children():
        if isinstance(widget, tk.Canvas):
            widget.destroy()

    #Limpiar tabla
    tabla.delete(*tabla.get_children())

    resultado1.config(text="")
    resultado2.config(text="")
        


#SONIDO DE LOS BOTONES
def Sonido_boton():
    mixer.init()  # Inicializar el módulo de sonido
    mixer.music.load("_internal/selectbutton-1.mp3")  # Cargar el archivo de sonido
    mixer.music.play()  # Reproducir el sonido

    mixer.music.set_endevent(mixer.USEREVENT)
    mixer.music.set_pos(0.0)
    mixer.music.get_pos()
    mixer.quit()

#Cerrar programa
def Salir():

    for widget in ventana.winfo_children():
        if widget != fondo_label:
            widget.destroy()

    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    x_centro = ancho_pantalla // 2
    y_centro = alto_pantalla // 2


    # Crear un nuevo Label con el mensaje
    mensaje = tk.Label(ventana, text="Cerrando la ventana...", font=("hooge 05_53", 20), justify="center",bg="#FEA43F", fg= 'white' )
    mensaje.pack(fill = tk.X)

    # Función para actualizar el texto con los puntos de carga
    def actualizar_puntos(puntos=0):
        mensaje.config(text="Cerrando la ventana" + "." * puntos)
        puntos = (puntos + 1) % 4
        ventana.after(500, actualizar_puntos, puntos)

    # Iniciar el efecto de carga
    actualizar_puntos()

    # Destruir la ventana después de 2 segundos
    ventana.after(2000, ventana.destroy)


#GUARDAR TABLA
def SaveTable():
    # Obtener los valores ingresados por el usuario
        A = float(VA.get())
        B = float(VB.get())
        C = float(VC.get())
        T = float(VT.get())

        A2 = float(VA2.get())
        B2 = float(VB2.get())
        C2 = float(VC2.get())
       
        # Calcular la presión de saturación 1
        P_saturacion1 = np.exp(A - (B / (T + C)))

        # Calcular la presión de saturación 2
        P_saturacion2 = np.exp(A2 - (B2 / (T + C2)))

        
        # Calcular las presiones para cada composición de mezcla
        X_especies1 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        X_especies2 = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
        P = [round(X1 * P_saturacion1 + X2 * P_saturacion2,3) for X1, X2 in zip(X_especies1, X_especies2)]
        Y1 = [round(X1*P_saturacion1/Pi, 3) for X1, Pi in zip(X_especies1, P)]

        df = pd.DataFrame({'X1':X_especies1,'X2':X_especies2,'Presión':P,'Y1':Y1})

        nombre_archivo = f"Puntodeburbujayderocio_{datetime.datetime.now():%Y%m%d_%H%M%S}.xlsx"

        #PON TU RUTA DONDE QUIERES QUE SE GUARDE EL ARCHIVO EXCEL
        ruta_directorio = filedialog.askdirectory()

        # Comprobar si el directorio existe, si no existe, crearlo
        if not os.path.exists(ruta_directorio):
            os.makedirs(ruta_directorio)

        # Crear la ruta completa del archivo
        ruta_completa = os.path.join(ruta_directorio, nombre_archivo)

        # Exportar el DataFrame a un archivo Excel en la ruta especificada
        df.to_excel(ruta_completa, index=False)

        print(f'Se ha creado el archivo "{nombre_archivo}" con éxito.')

#INICIO DE SESION
def guardar_sesion():
    with open("_internal/_log.txt", "a") as archivo:
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"Sesion iniciada el {fecha_hora}\n")

def ClearLog_():

    def actualizar_puntos1(puntos=0):
        resultado1.config(text="Limpiando registro" + "." * puntos, fg='green')
        puntos = (puntos + 1) % 4
        if puntos == 0:  # Si se completaron los puntos, limpiar el archivo
            resultado1.config(text="")
            with open("_internal/_log.txt", "w") as archivo:
                archivo.write("")
        else:  # Si no se han completado los puntos, continuar actualizando el mensaje
            ventana.after(800, actualizar_puntos1, puntos)

    actualizar_puntos1()  # Iniciar el proceso de actualización



##
def presionar_boton1(event):
    boton1.config(relief=tk.SUNKEN, bg = 'white', fg ='black')
    calcular_presion()
    Sonido_boton()
def soltar_boton1(event):
    boton1.config(relief=tk.RAISED, bg = "#FFB458", fg = "WHITE" )

##
def presionar_f4(event):
    boton2.config(relief=tk.SUNKEN, bg = 'white', fg ='black')
    Limpiarvalores()
    Sonido_boton()
def soltar_f4(event):
    boton2.config(relief=tk.RAISED, bg = "#FFB458", fg = "WHITE" )
  
    


##
def presionar_f2(event):
    boton3.config(relief=tk.SUNKEN, bg = 'white', fg ='black')
    Salir()
    Sonido_boton()
def soltar_f2(event):
    boton3.config(relief=tk.RAISED, bg = "#FFB458", fg = "WHITE" )


def Iniciar():
    # Crea una nueva ventana
    segunda_ventana = tk.Toplevel(ventana_inicio)
    # Configura la nueva ventana
    segunda_ventana.title("TERMODINAMICA by Daniel Silva")
    # Oculta la ventana inicial
    
    ventana_inicio.withdraw()
    # Destruye la ventana inicial después de un tiempo
    

    ventana_inicio.after(0, ventana_inicio.destroy)
    
def presionar_botonINICIAR(event):
    Iniciar_bot.config(relief=tk.SUNKEN, bg = 'white', fg ='black')
    Iniciar()
    Sonido_boton()
def soltar_botonINICIAR(event):
    Iniciar_bot.config(relief=tk.RAISED, bg = "#FFB458", fg = "WHITE" )

def SalirVentana1():

    for widget in ventana_inicio.winfo_children():
        if widget != fondo_label:
            widget.destroy()


    
    mensaje = tk.Label(ventana_inicio, text="Cerrando la ventana...", font=("hooge 05_53", 20),bg="#FEA43F", fg= 'white' )
    mensaje.pack(fill = tk.X)


    ventana_inicio.withdraw()
    ventana_inicio.quit()

    import sys
    sys.exit()
    return

    
    


def presionar_f2Ventana1(event):
    botonsalir.config(relief=tk.SUNKEN, bg = 'white', fg ='black')
    SalirVentana1()
    Sonido_boton()
def soltar_f2Ventana1(event):
    botonsalir.config(relief=tk.RAISED, bg = "#FFB458", fg = "WHITE" )



def on_closing():
    pass 







def Explicacion():
    
    mensaje = tk.Toplevel(ventana_inicio)
    ruta_icono = "_internal/Iconoaplicacion_1.ico"
    mensaje.iconbitmap(ruta_icono)

    # Cargar la imagen de fondo
    imagen_fondo = tk.PhotoImage(file="_internal/ds.png")

    # Crear una etiqueta con la imagen de fondo
    fondo_label = tk.Label(mensaje, image=imagen_fondo)
    fondo_label.image = imagen_fondo  # Guardar una referencia a la imagen de fondo
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)


    mensaje.title("Explicacion")
    mensaje.geometry("800x600")
    Botonesexp = Label(mensaje, text="<Enter> - Iniciar, Calcular \n <F1> - Limpiar registro \n <F4> - Limpiar valores \n <F2> - Cerrar aplicación \n <F11> - Pantalla completa \n <Esc> - Salir de pantalla completa \n \n", fg="WHITE", font=("hooge 05_55", 16), bg="#FEA43F")
    Botonesexp.pack()
    Botonesexp.place(relx=0.5, rely=0.5, anchor=CENTER)
    ventana_inicio.update()  # Actualiza la ventana principal para que el mensaje emergente se muestre inmediatamente


    def actualizar_cuenta_regresiva(segundos_restantes):
        if segundos_restantes > 0:
            Botonesexp.config(text=f"<Enter> - Iniciar, Calcular \n <F1> - Limpiar registro \n <F4> - Limpiar valores \n <F2> - Cerrar aplicación \n <F11> - Pantalla completa \n <Esc> - Salir de pantalla completa \n \nCerrando en {segundos_restantes} segundos")
            ventana_inicio.after(1000, lambda: actualizar_cuenta_regresiva(segundos_restantes - 1))
        else:
            mensaje.destroy()

    segundos_restantes = 10
    actualizar_cuenta_regresiva(segundos_restantes)
     





    


################################################        VENTANA DE INICIO    #################################################################



ventana_inicio = tk.Tk()
ventana_inicio.title("Termodinamica")
ventana_inicio.protocol("WM_DELETE_WINDOW", SalirVentana1)

ventana_inicio.geometry("1366x768")
ventana_inicio.resizable(0,0)

ruta_icono = "_internal/Iconoaplicacion_1.ico"
ventana_inicio.iconbitmap(ruta_icono)


# Cargar la imagen de fondo
imagen_fondo = PhotoImage(file="_internal/ds.png")

# Crear una etiqueta con la imagen de fondo
fondo_label = tk.Label(ventana_inicio, image=imagen_fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)


Titulo = tk.Label(ventana_inicio, text="TERMODINAMICA DE EQUILIBRIO Y SOLUCIONES", bg="#FEA43F", font=("hooge 05_53", 30), fg="WHITE")
Titulo.pack(fill=tk.X)


#BOTON DE INICIO
Iniciar_bot = tk.Button(ventana_inicio ,text='INICIAR', padx = 10, pady= 5, command = lambda: [Iniciar(), Sonido_boton()], bg = "#FFB458", 
                   fg = "WHITE", font = ("hooge 05_53", 15) )

Iniciar_bot.pack()
Iniciar_bot.place(relx = 0.5, rely = 0.5)


Infobut = tk.Button(ventana_inicio, text="Info.", padx = 10, command= lambda: [Explicacion(), Sonido_boton()], pady= 5, bg = "#FFB458", 
                   fg = "WHITE", font = ("hooge 05_55", 15) )
Infobut.pack()
Infobut.place(relx=0.89, rely=0.99, anchor='se')

#boton Salir
botonsalir = tk.Button(ventana_inicio, text="SALIR", padx = 10, command= lambda: [SalirVentana1(),Sonido_boton()], pady= 5, bg = "#FFB458", 
                   fg = "WHITE", font = ("hooge 05_55", 15) )
botonsalir.pack(pady=10)
botonsalir.place(relx=0.99, rely=0.99, anchor='se')


ventana_inicio.bind("<KeyPress-F2>", presionar_f2Ventana1)
ventana_inicio.bind("<KeyRelease-F2>", soltar_f2Ventana1)

def toggle_fullscreen(event):
    ventana_inicio.focus_set()
    ventana_inicio.attributes("-fullscreen", True)

def exit_fullscreen(event):
    ventana_inicio.attributes("-fullscreen", False)

ventana_inicio.bind("<F11>", toggle_fullscreen)
ventana_inicio.bind("<Escape>", exit_fullscreen)
ventana_inicio.bind("<KeyPress-Return>", presionar_botonINICIAR)
ventana_inicio.bind("<KeyRelease-Return>", soltar_botonINICIAR)



Madeby1 = tk.Label(ventana_inicio, text='Made by: Daniel Silva', font = ('hooge 05_55', 20), fg='white', bg = '#FF9E1E')
Madeby1.pack()
Madeby1.place(relx=0.3, rely=0.99, anchor='se')


ventana_inicio.protocol("WM_DELETE_WINDOW", on_closing)
ventana_inicio.mainloop()



##########################################################        VENTANA PRINCIPAL         ##############################################
ventana = tk.Tk()

# Cargar la imagen de fondo
imagen_fondo = PhotoImage(file="_internal/ds.png")

# Crear una etiqueta con la imagen de fondo
fondo_label = tk.Label(ventana, image=imagen_fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)


guardar_sesion()
ventana.title("Termodinamica")
ventana.geometry("1600x900")
ventana.resizable(0,0)

ruta_icono = "_internal/Iconoaplicacion_1.ico"
ventana.iconbitmap(ruta_icono)

#CONFIGURACION DE TABLAS
style = ttk.Style()
style.configure('Treeview', font=('Calibri Light', 10))
style.configure('Treeview.Heading', font=('hooge 05_53', 12, 'bold'), background="YELLOW", foreground="BLACK")



# TITULO DEL PROGRAMA
Titulo = tk.Label(ventana, text="SOLUCIONES IDEALES", justify="center",bg="#FEA43F", font=("hooge 05_53", 20), fg = "WHITE")
Titulo.pack(fill = tk.X)




#A
Constante_A = tk.Label(ventana, text = "A Sustancia 1",fg = "WHITE",font=("hooge 05_55", 16),bg="#FEA43F")
Constante_A.pack()
Constante_A.place(relx=0.0602, rely=0.1111)

#CAJA A
VA = tk.Entry(ventana,highlightthickness=2, highlightbackground="#FAB361", font=("hooge 05_53", 12))
VA.pack()
VA.place(relx=0.0602, rely=0.1444)

#B
Constante_B = tk.Label(ventana, text = "B Sustancia 1",fg = "WHITE",font=("hooge 05_55", 16),bg="#FEA43F")
Constante_B.pack()
Constante_B.place(relx= 0.0602,rely= 0.2)

#Caja B
VB = tk.Entry(ventana, highlightthickness=2, highlightbackground="#FAB361", font=("hooge 05_53", 12))
VB.pack()
VB.place(relx=0.0602, rely=0.2333)

#C Sustancia 1
Constante_C = tk.Label(ventana, text = "C Sustancia 1",fg = "WHITE",font=("hooge 05_55", 16),bg="#FEA43F")
Constante_C.pack()
Constante_C.place(relx = 0.06024096386, rely = 260/900)

#Caja C
VC = tk.Entry(ventana, highlightthickness=2, highlightbackground="#FAB361", font=("hooge 05_53", 12))
VC.pack()
VC.place(relx=100/1660,rely=290/900)

#Temperatura en 
cT = tk.Label(ventana, text = "Temperatura (K)",fg = "WHITE",font=("hooge 05_55", 16),bg="#FEA43F")
cT.pack()
cT.place(relx = 100/1660, rely = 340/900)

#Caja Temperatura
VT = tk.Entry(ventana, highlightthickness=2, highlightbackground="#FAB361", font=("hooge 05_53", 12))
VT.pack()
VT.place(relx=100/1660,rely=370/900)

#A2
Constante_A2 = tk.Label(ventana, text = "A Sustancia 2",fg = "WHITE",font=("hooge 05_55", 16),bg="#FEA43F")
Constante_A2.pack()
Constante_A2.place(relx = 400/1660, rely = 100/900)

#CAJA A2
VA2 = tk.Entry(ventana, highlightthickness=2, highlightbackground="#FAB361", font=("hooge 05_53", 12))
VA2.pack()
VA2.place(relx=400/1660, rely=130/900)

#B2
Constante_B2 = tk.Label(ventana, text = "B Sustancia 2",fg = "WHITE",font=("hooge 05_55", 16),bg="#FEA43F")
Constante_B2.pack()
Constante_B2.place(relx = 400/1660, rely = 180/900)

#Caja B2
VB2 = tk.Entry(ventana, highlightthickness=2, highlightbackground="#FAB361", font=("hooge 05_53", 12))
VB2.pack()
VB2.place(relx=400/1660,rely=210/900)

#C Sustancia 2
Constante_C2 = tk.Label(ventana, text = "C Sustancia 2",fg = "WHITE",font=("hooge 05_55", 16),bg="#FEA43F")
Constante_C2.pack()
Constante_C2.place(relx = 400/1660, rely = 260/900)

#Caja C2
VC2 = tk.Entry(ventana, highlightthickness=2, highlightbackground="#FAB361", font=("hooge 05_53", 12))
VC2.pack()
VC2.place(relx=400/1660,rely=290/900)

#########################################
canvas_frame = tk.Frame(ventana, bd=0, relief=tk.SOLID, width=400, height=400, highlightbackground ="#BC7801",highlightthickness=4)
canvas_frame.place(relx=1200/1660,rely=370/900)

# Obtener el ancho total del Frame
ancho_total = canvas_frame.winfo_width()

# Obtener el ancho interno del Frame
ancho_interno = canvas_frame.winfo_reqwidth()

# Calcular el ancho del borde
ancho_borde = ancho_total - ancho_interno
grosor_borde = canvas_frame.cget("highlightthickness")
##########################################

ancho_ventana = ventana.winfo_reqwidth()
alto_ventana = ventana.winfo_reqheight()

#Boton Calcular
boton1 = tk.Button(ventana, text="CALCULAR", padx = 10, pady= 5, command = lambda: [calcular_presion(), Sonido_boton()], bg = "#FFB458", 
                   fg = "WHITE", font = ("hooge 05_55", 15))
boton1.pack(pady=10)


boton1.place(relx=400/1660 , rely=350/900)

#Boton Limpiar
boton2 = tk.Button(ventana, text="LIMPIAR", padx = 10, command= lambda: [Limpiarvalores(),Sonido_boton() ], 
                   pady= 5, bg = "#FFB458", fg = "WHITE", font = ("hooge 05_55", 15), )
boton2.pack(pady=10)
boton2.place(relx=550/1660, rely = 350/900)

#boton Salir
boton3 = tk.Button(ventana, text="SALIR", padx = 10, command= lambda: [Salir(),Sonido_boton()], pady= 5, bg = "#FFB458", 
                   fg = "WHITE", font = ("hooge 05_55", 15), )
boton3.pack(pady=10)
boton3.place(relx=1500/1660,rely=800/900)



#Guardar grafica
Guardargraf = tk.Button(ventana, text ='GUARDAR GRAFICA', 
                        command= lambda: [GuardarGrafica(),Sonido_boton()], pady= 5, bg = "#FFB458", fg = "WHITE", font = ("hooge 05_55", 16) )
Guardargraf.pack(pady=10)
Guardargraf.place(relx=1204/1660, rely=800/900)


resultado1 = tk.Label(ventana, text="", fg="GREEN", bg ='white', font = ('hooge 05_55',12))
resultado2 = tk.Label(ventana, text="", fg="GREEN", bg ='white', font = ('hooge 05_55',12))
resultado1.pack()  # Muestra el Label
resultado2.pack()
resultado1.place(relx=100/1660, rely=465/900)
resultado2.place(relx=100/1660, rely=500/900)


#BOTON PARA GUARDAR TABLA
GuardarTabla = tk.Button(ventana, text ='GUARDAR TABLA', 
                         command= lambda: [SaveTable(),Sonido_boton()], pady= 5, bg = "#FFB458", fg = "WHITE", font = ("hooge 05_55", 15))
GuardarTabla.pack()
GuardarTabla.place(relx = 1200/1660, rely = 305/900)



#CREAR TABLA
tabla = ttk.Treeview(ventana)
tabla.pack(expand=True, fill=tk.BOTH)


# Configurar columnas
tabla["columns"] = ("X1", "X2", "Y1", "P(kPa)")

tabla.column('#0', width=0, stretch=tk.NO)
tabla.column('X1', anchor=tk.W, width=100, stretch=tk.NO)
tabla.column('X2', anchor=tk.CENTER, width=100,stretch=tk.NO)
tabla.column('Y1', anchor=tk.W, width=100,stretch=tk.NO)
tabla.column('P(kPa)', anchor=tk.W, width=100,stretch=tk.NO)

# Configurar encabezados de columnas
tabla.heading("X1", text="X1", anchor=tk.W)
tabla.heading("X2", text="X2", anchor=tk.W)
tabla.heading("Y1", text="Y1", anchor=tk.W)
tabla.heading("P(kPa)", text="P(kPa)", anchor=tk.W)

tabla.bind("<Button-1>", lambda e: "break")

tabla.pack()
tabla.place(relx = 1200/1660, rely = 52/900)


ventana.bind("<F11>", lambda event: ventana.attributes("-fullscreen", True))
ventana.bind("<Escape>", lambda event: ventana.attributes("-fullscreen", False))

ventana.bind("<KeyPress-Return>", presionar_boton1)
ventana.bind("<KeyRelease-Return>", soltar_boton1)


ventana.bind("<KeyPress-F4>", presionar_f4)
ventana.bind("<KeyRelease-F4>", soltar_f4)

ventana.bind("<F1>", lambda event:ClearLog_())


ventana.bind("<KeyPress-F2>", presionar_f2)
ventana.bind("<KeyRelease-F2>", soltar_f2)


Madeby = tk.Label(ventana, text='Made by: Daniel Silva', font = ('hooge 05_55', 20), fg='white', bg = '#FF9E1E')
Madeby.pack()
Madeby.place(relx=100/1660, rely=800/900)






# Mostrar la ventana
ventana.mainloop()
