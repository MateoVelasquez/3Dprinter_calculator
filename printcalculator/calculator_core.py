"""Módulo principal

Contiene las funciones de calculo del programa.
"""
import os
import configparser
import shutil
from pathlib import Path, PurePath
from math import pi
from typing import Dict, Optional

# Obteniendo ruta APPDATA/LOCAL
APPDATAFOLDER = (Path(os.getenv('LOCALAPPDATA')).joinpath('3Dprincoscal'))
# Rutas de los archivos de configuración.
DEFAULT_INI_PATH = PurePath(__file__).parent.joinpath('config.ini')
INI_PATH = APPDATAFOLDER.joinpath('config.ini')


def verify_config_folder(defaultini=DEFAULT_INI_PATH,
                         configpath=INI_PATH,
                         folderconfig=APPDATAFOLDER):
    """Verificar folder de configuración.

    Verifica la existencia de la carpeta de configuración en APPDATA/Local.
    En caso de no existir, se crea junto con una copia de la configuración.

    Parameters
    ----------
    defaultini: str
        Ruta del archivo de configuración por defecto.
    configpath: str
        Ruta de salida del archivo de configuración.
    folderconfig: str
        Ruta de la carpeta de configuración.
    """
    if not folderconfig.exists():
        # Creando carpeta de la calculadora si no existe.
        folderconfig.mkdir(parents=True, exist_ok=True)
    if not configpath.is_file():
        # Copiando config.ini si no existe en esa ubicación.
        shutil.copy(str(defaultini), str(configpath))


def language_dic() -> Dict:
    """Diccionario de lenguaje.

    Exporta un diccionario de lenguaje.

    Returns
    -------
    dict:
        Diccionario de lenguaje.
    """
    text_dic = {
        'MATERIAL_COST': "Costo del Material ($ / Kg)",
        'MATERIAL_DENSITY': 'Densidad del material (gr / cm^3)',
        'SPOOL_WEIGTH': 'Peso del núcleo de la bobina (gr)',
        'ELECTRIC_COST': 'Costo Eléctrico ( $ KW/h)',
        'PRINTER_POWER': 'Potencia de la impresora (W)',
        'PRINTER_PRICE': 'Precio de la impresora ($)',
        'AMORTIZATION': 'Amortización de la máquina (años)',
        'DAILY_PRINTER_TIME': 'Uso diario de la máquina (h)',
        'FAILURE_RATE': 'Porcentaje de fallos (%)',
        'WORKFORCE_COST': 'Costo de mano de obra',
        'ACCEPT': 'Aceptar',
        'CANCEL': 'Cancelar',
        'MAIN_TITLE': 'Calculadora de impresión 3D',
        'HOURS': 'Horas de impresión',
        'MINUTES': 'Minutos de impresión',
        'MATERIAL': 'Cantidad del material',
        'WORKMANTIME': 'Horas de mano de obra',
        'CALCULATE': 'Calcular',
        'MAT_UNIT': 'Unidad de medida del material'
    }
    return text_dic


def read_ini(rutaconfigpr=str(INI_PATH)) -> Dict:
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


def modify_config_values(new_vals_dic,
                         rutaconfigpr=str(INI_PATH)) -> Optional[str]:
    """Modificar valores de configuración.

    Modificar valores de configuración.

    Parameters
    ----------
    new_vals_dic: dict
        Diccionario de valores a modificar
    rutaconfigpr: str
        Ruta del archivo de configuración a modificar.

    Returns
    -------
    Optional:
        Str con mensaje de error si falla, None si no hay errores.
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


def calculate_cost(hrs: int, mins: int, workhrs: float,
                   material: float) -> int:
    """Calcular costo.

    Función para calcular el costo de la impresión 3D.

    Parameters
    ----------
    hrs: int
        Hora estimada de impresión.
    mins: int
        Minutos estimados de impresión.
    workhrs: float
        Tiempo de mano de obra dedicado.
    material: float
        Material gastado en milímetros.
    cfgdic_in: Dict
        Diccionario de parámetros de configuración.

    Returns
    -------
    int:
        Costo total de la impresión 3D en la unidad configurada.
    """
    cfgdic = read_ini()['CONFIGURATION']
    mat_in_mm = bool(int(cfgdic['IN_MM']))
    # Calculando los gramos de material.
    if mat_in_mm:
        gr = (float(cfgdic['MATERIAL_DENSITY']) * pi * (1.75 / 20)**2 *
              material / 10)
    else:
        gr = material
    # Calculando tiempo completo de impresión:
    totalh = hrs + (mins / 60)
    # Calculando costo eléctrico.
    eleccost = (int(cfgdic['ELECTRIC_COST']) / 1000 * totalh *
                int(cfgdic['PRINTER_POWER']))
    # Calculando costo de material.
    matcost = gr * (int(cfgdic['MATERIAL_COST']) /
                    (1000 - int(cfgdic['SPOOL_WEIGTH'])))
    # Calculando costo de mano de obra:
    workmancost = workhrs * int(cfgdic['WORKFORCE_COST'])
    # Calculando amortización de la maquina. 300 equivale a Num. de dias en uso
    amort = (int(cfgdic['PRINTER_PRICE']) /
             (int(cfgdic['AMORTIZATION']) * 300 *
              int(cfgdic['DAILY_PRINTER_TIME']))) * totalh
    # Sumando costo total de impresion.
    totalimpcost = eleccost + matcost + workmancost + amort
    # Calculando sobre porcentaje de fallas
    totalimpcost = totalimpcost * (1 + int(cfgdic['FAILURE_RATE']) / 100)
    return int(round(totalimpcost, 0))
