"""Interfaz de configuracion.
"""
import tkinter as tk
from tkinter import messagebox
import calculator_core


def createtextbox(configwindow, config_dic):
    """Crear cajas de texto.

    Funcion para crear las cajas de texto y almacenar valores.
    """
    if 'IN_MM' in config_dic:
        config_dic.pop('IN_MM')
    text_dic = calculator_core.language_dic()
    textbox = {}
    for i, (key, value) in enumerate(config_dic.items()):
        # Crear caja de texto
        tk.Label(configwindow, text=text_dic[key]).grid(row=i + 2, column=0)
        tbox = tk.Entry(configwindow)
        tbox.insert(0, value)
        tbox.grid(row=i + 2, column=1)
        textbox[key] = tbox
    tk.Label(configwindow, text='').grid(column=0)
    return textbox, i + 2


def acept_button_fn(congigwindow, entry_obs):
    """Funcion de boton aceptar

    Contiene la rutina a realizar por el botón aceptar.
    """
    newdic = {}
    for key, objs in entry_obs.items():
        newdic[key] = objs.get()
    status = calculator_core.modify_config_values(newdic)
    if status:
        messagebox.showerror("Error almacenando parámetros", status)
    else:
        congigwindow.destroy()


def radiob1():
    status = calculator_core.modify_config_values({'IN_MM': 0})
    if status:
        messagebox.showerror("Error almacenando parámetros", status)
    pass


def radiob2():
    status = calculator_core.modify_config_values({'IN_MM': 1})
    if status:
        messagebox.showerror("Error almacenando parámetros", status)
    pass


def create_buttons(configwindow, inframe, entry_obs, place):
    """Crear botones

    Crea botones en la ventana de configuracion.
    """
    text_dic = calculator_core.language_dic()
    tk.Button(inframe,
              text=text_dic['ACCEPT'],
              command=lambda: acept_button_fn(configwindow, entry_obs)).grid(
                  row=place + 2, column=0)
    tk.Button(inframe,
              text=text_dic['CANCEL'],
              command=configwindow.destroy).grid(row=place + 2, column=1)


def create_radiobuttons(frameparent, conf_dic):
    text_dic = calculator_core.language_dic()
    label_text = f"{text_dic['MAT_UNIT']}:          "
    tk.Label(frameparent, text=label_text).grid(row=0, column=0)
    rb1 = tk.Radiobutton(frameparent, text="gr",
                         value=1, command=radiob1)
    rb1.grid(row=0, column=1)
    rb2 = tk.Radiobutton(frameparent, text="mm",
                         value=2, command=radiob2)
    rb2.grid(row=0, column=2)
    if bool(int(conf_dic['IN_MM'])):
        rb2.select()
    else:
        rb1.select()


def main(window):
    # Leer configuracion ini.
    config_dic = calculator_core.read_ini()['CONFIGURATION']
    # Crear GUI
    confg = tk.Toplevel(window)
    confg.title("configuration")
    confg.geometry("350x320+124+124")
    # Crear titulo
    tk.Label(confg, text='CONFIGURACION', font='Helvetica 18 bold').pack()
    # Crear radiobotones
    radiobframe = tk.Frame(confg)
    radiobframe.pack()
    create_radiobuttons(radiobframe, config_dic)
    # Crear entradas
    inframe = tk.Frame(confg)
    inframe.pack()
    inbox, place = createtextbox(inframe, config_dic)
    # Crear botones de aceptar y cancelar
    create_buttons(confg, inframe, inbox, place)
