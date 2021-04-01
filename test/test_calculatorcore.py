import os
import sys
ruta = os.path.abspath(os.path.normpath('.\\printcalculator'))
sys.path.append(ruta)
import calculator_core #noqa


def test_modifyconfig():
    dic_test = {
        'MATERIAL_COST': '70000',
        'FAILURE_RATE': '10'
    }
    calculator_core.modify_config_values(dic_test)


test_modifyconfig()
