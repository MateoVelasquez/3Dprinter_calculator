"""Módulo principal

Contiene las funciones de calculo del programa.
"""
import configparser
from pathlib import PurePath
from math import pi
# from typing import Optional, Dict

INI_PATH = PurePath(__file__).parent.joinpath('config.ini')


def language_dic():
    text_dic = {
        'MATERIAL_COST': "Costo del Material ($ / Kg)",
        'MATERIAL_DENSITY': 'Densidad del material (gr / cm^3)',
        'SPOOL_WEIGTH': 'Peso del nucleo de la bobina (gr)',
        'ELECTRIC_COST': 'Costo Eléctrico ( $ KW/h)',
        'PRINTER_POWER': 'Potencia de la impresora (W)',
        'PRINTER_PRICE': 'Precio de la impresora ($)',
        'AMORTIZATION': 'Amortizacion de la máquina (años)',
        'DAILY_PRINTER_TIME': 'Uso diario de la máquina (h)',
        'FAILURE_RATE': 'Porcentaje de fallos (%)',
        'WORKFORCE_COST': 'Costo de mano de obra',
        'ACCEPT': 'Aceptar',
        'CANCEL': 'Cancelar',
        'MAIN_TITLE': 'Calculadora de impresion 3D',
        'HOURS': 'Horas de impresion',
        'MINUTES': 'Minutos de impresion',
        'MATERIAL': 'Cantidad del material',
        'WORKMANTIME': 'Horas de mano de obra',
        'CALCULATE': 'Calcular',
        'MAT_UNIT': 'Unidad de medida del material'
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


def calculate_cost(hrs: int, mins: int, workhrs: float, material: float):
    """Calcular costo.

    Función para calcular el costo de la impresion 3D

    Parameters
    ----------
    hrs: int
        Hora estimada de impresión.
    mins: int
        Minutos estimados de impresión.
    workhrs: float
        Tiempo de mano de obra dedicado.
    material: float
        Material gastado en milimetros.
    cfgdic_in: Dict
        Diccionario de parametros de configuracion.

    Returns
    -------
    int:
        Costo total de la impresion 3D en la unidad configurada.
    """
    cfgdic = read_ini()['CONFIGURATION']
    mat_in_mm = bool(int(cfgdic['IN_MM']))
    # Calculando los gramos de material.
    if mat_in_mm:
        gr = (float(cfgdic['MATERIAL_DENSITY']) * pi * (1.75 / 20)**2 *
              material / 10)
    else:
        gr = material
    # Calculando tiempo completo de impresion:
    totalh = hrs + mins / 60
    # Calculando costo electrico.
    eleccost = int(cfgdic['ELECTRIC_COST']) / 1000 * totalh
    # Calculando costo de material.
    matcost = gr * (int(cfgdic['MATERIAL_COST']) /
                    (1000 - int(cfgdic['SPOOL_WEIGTH'])))
    # Calculando costo de mano de obra:
    workmancost = workhrs * int(cfgdic['WORKFORCE_COST'])
    # Calculando amortizacion de la maquina.
    amort = (int(cfgdic['PRINTER_PRICE']) /
             (int(cfgdic['AMORTIZATION']) * 250 *
              int(cfgdic['DAILY_PRINTER_TIME'])))
    totalimpcost = eleccost + matcost + workmancost + amort
    # Calculando sobre porcentaje de fallas
    totalimpcost = totalimpcost * (1 + int(cfgdic['FAILURE_RATE']) / 100)
    return int(round(totalimpcost, 0))
