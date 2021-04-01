"""Interfaz 3d print calculator.

Módulo que contiene la interfaz del aplicativo.
"""
import tkinter as tk
import calculator_core
import config_gui

# Cargando parametros
PARAM_DIC = calculator_core.read_ini()
# Creacion de ventana principal
window = tk.Tk()
window.geometry("300x300+100+100")
window.title('3Dprint Calculator')
# Creacion de la barra menú.
menu_bar = tk.Menu(window)
# Creacion del menú archivo
file_menu = tk.Menu(menu_bar)
file_menu.add_command(
    label='Configurar',
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


# BOTONES:
# Boton para abrir opciones:

window.mainloop()
