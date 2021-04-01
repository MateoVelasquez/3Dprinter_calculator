"""Interfaz de configuracion.
"""
import tkinter as tk
from tkinter import messagebox
import calculator_core


def createtextbox(configwindow, config_dic):
    """Crear cajas de texto.

    Funcion para crear las cajas de texto y almacenar valores.
    """
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


def get_config_values(buttons_def):

    pass


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


def create_buttons(configwindow, entry_obs, place):
    """Crear botones

    Crea botones en la ventana de configuracion.
    """
    text_dic = calculator_core.language_dic()
    tk.Button(configwindow,
              text=text_dic['ACCEPT'],
              command=lambda: acept_button_fn(configwindow, entry_obs)).grid(
                  row=place + 2, column=0)
    tk.Button(configwindow,
              text=text_dic['CANCEL'],
              command=configwindow.destroy).grid(row=place + 2, column=1)


def main(window):
    # Leer configuracion ini.
    config_dic = calculator_core.read_ini()['CONFIGURATION']
    # Crear GUI
    confg = tk.Toplevel(window)
    confg.title("configuration")
    confg.geometry("350x300+124+124")
    tk.Label(confg, text='CONFIGURACION', font='Helvetica 18 bold').grid(row=0)
    inbox, place = createtextbox(confg, config_dic)
    create_buttons(confg, inbox, place)
