"""Interfaz 3d print calculator.

Módulo que contiene la interfaz del aplicativo.
"""
import tkinter as tk
from tkinter import messagebox
import calculator_core
import config_gui


def numbervalidation(S):
    if S in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        resulttext.set('')
        return True
    entryframe.bell()
    return False


def calculatebuttonfn():
    # obteniendo valores de botones
    try:
        hours = int(hourentry.get())
        mins = int(minentry.get())
        workmanhour = float(workentry.get())
        mater = float(matentry.get())
        total_cost = calculator_core.calculate_cost(hours, mins, workmanhour,
                                                    mater)
        resulttext.set(f'El costo de la impresion es de ${total_cost}')
    except Exception as e:
        messagebox.showerror("Error calculando coste", e)
    pass


# Cargando parametros
PARAM_DIC = calculator_core.read_ini()
# Cargando lenguaje
lang_dic = calculator_core.language_dic()
# Creacion de ventana principal
window = tk.Tk()
window.geometry("300x260+100+100")
window.title('3Dprint Calculator')
# Creacion de la barra menú.
menu_bar = tk.Menu(window)
# Creacion del menú archivo
file_menu = tk.Menu(menu_bar)
file_menu.add_command(label='Configurar',
                      command=lambda: config_gui.main(window))
file_menu.add_command(label='Exportar')
file_menu.add_separator()
file_menu.add_command(label='Salir', command=window.destroy)
# Creacion del menú help.
help_menu = tk.Menu(menu_bar)
help_menu.add_command(label='Acerca de')
# Agregando menus a la barra.
menu_bar.add_cascade(label="Archivo", menu=file_menu)
menu_bar.add_cascade(label="Ayuda", menu=help_menu)
window.config(menu=menu_bar)

# marco superior para titulos
frame = tk.Frame(window, width=300, height=40)
frame.pack()
tk.Label(frame, text=lang_dic['MAIN_TITLE'], font='Helvetica 14 bold').pack()

# Texto variable para almacenar el resultado:
resulttext = tk.StringVar()
resulttext.set('')

#  ---------------- Marco para Entradas.
entryframe = tk.Frame(window, width=300, height=100)
entryframe.pack()
# Horas
tk.Label(entryframe, text=lang_dic['HOURS'],
         font='Helvetica 11').grid(row=0, column=0)
vcmd = (entryframe.register(numbervalidation), '%S')
hourentry = tk.Entry(entryframe, width=10, validate='key', vcmd=vcmd)
hourentry.insert(0, 0)
hourentry.grid(row=0, column=1)
# Minutos
tk.Label(entryframe, text=lang_dic['MINUTES'],
         font='Helvetica 11').grid(row=1, column=0)
minentry = tk.Entry(entryframe, width=10, validate='key', vcmd=vcmd)
minentry.insert(0, 0)
minentry.grid(row=1, column=1)
# Cantidad de material
tk.Label(entryframe,
         text=f"{lang_dic['MATERIAL']}",
         font='Helvetica 11').grid(row=2, column=0)
matentry = tk.Entry(entryframe, width=10, validate='key', vcmd=vcmd)
matentry.insert(0, 0)
matentry.grid(row=2, column=1)
# Tiempo de mano de obra.
tk.Label(entryframe, text=lang_dic['WORKMANTIME'],
         font='Helvetica 11').grid(row=3, column=0)
workentry = tk.Entry(entryframe, width=10, validate='key', vcmd=vcmd)
workentry.insert(0, 0)
workentry.grid(row=3, column=1)

# ----- CREACION DE BOTON CALCULAR
spaceframe = tk.Frame(window, width=300, height=30)
spaceframe.pack()
buttonframe = tk.Frame(window, width=300, height=100)
buttonframe.pack()
calculatebutton = tk.Button(buttonframe,
                            text=lang_dic['CALCULATE'],
                            font='Helvetica 14 bold',
                            command=lambda: calculatebuttonfn())
calculatebutton.pack()

# ---- CREACION DE TEXTO RESULTADO
spaceframe2 = tk.Frame(window, width=300, height=20)
spaceframe2.pack()
labelframe = tk.Frame(window, width=300, height=50)
labelframe.pack()

resultlabel = tk.Label(labelframe,
                       textvariable=resulttext,
                       font='Helvetica 11 bold')
resultlabel.pack(side=tk.BOTTOM)

# ---- EJECUTANDO PROGRAMA
window.mainloop()
