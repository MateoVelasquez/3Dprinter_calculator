"""Módulo principal

Contiene las funciones de calculo del programa.
"""
import configparser
from pathlib import PurePath
# from typing import Optional


INI_PATH = PurePath(__file__).parent.joinpath('config.ini')


def language_dic():
    text_dic = {
        'MATERIAL_COST': "Costo del Material ($ / Kg)",
        'MATERIAL_DENSITY': 'Densidad del material (gr / cm^3)',
        'SPOOL_WEIGTH': 'Peso de la bobina (gr)',
        'ELECTRIC_COST': 'Costo Eléctrico ( $ KW/h)',
        'PRINTER_POWER': 'Potencia de la impresora (W)',
        'PRINTER_PRICE': 'Precio de la impresora ($)',
        'AMORTIZATION': 'Amortizacion de la máquina (años)',
        'DAILY_PRINTER_TIME': 'Uso diario de la máquina (h)',
        'FAILURE_RATE': 'Porcentaje de fallos (%)',
        'WORKFORCE_COST': 'Costo de mano de obra',
        'ACCEPT': 'Aceptar',
        'CANCEL': 'Cancelar'
    }
    return text_dic


def read_ini(rutaconfigpr=INI_PATH):
    """Lee parámetros de configuración.

    Dado un archivo de configuración .ini, se leen los parámetros
    y se devuelven como un diccionario.
    Parameters
    ----------
    rutaconfigpr: str
        Ruta del archivo de configuración de parámetros.
    Returns
    -------
    parametros_dic: dict
        Diccionario de parámetros extraídos del archivo Config.ini
    """
    parametros_dic = {}
    cfg = configparser.ConfigParser()
    lect = cfg.read(rutaconfigpr)
    if not lect:
        print('Error leyendo el archivo de parámetros.')
    else:
        for section in cfg.sections():
            parametros_dic[section] = {}
            for option in cfg.options(section):
                parametros_dic[section][option.upper()] = cfg[section][option]
    return parametros_dic


def modify_config_values(new_vals_dic, rutaconfigpr=INI_PATH):
    """Modificar valores

    Modificar valores de configuracion.
    """
    errs = None
    try:
        cfgw = configparser.RawConfigParser()
        cfgw.optionxform = str
        cfgw.read(rutaconfigpr)
        for key, val in new_vals_dic.items():
            cfgw.set('CONFIGURATION', key, val)
        with open(rutaconfigpr, 'w') as configfile:
            cfgw.write(configfile)
    except Exception as e:
        msg = f'Error almacenando valores: {e}'
        errs = msg
        print(msg)
    return errs


def calculate_cost():
    """Calcular costo.

    Función para calcular el costo de la impresion 3D
    """
    print('hola mundo')
    return None
