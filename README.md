# 3Dprinter_calculator
Desarrollo de una calculadora de costos para impresiones 3D.
La finalidad de este proyecto es realizar un aplicativo que calcule el estimado de cuanto pueden costar las piezas impresas en 3D, de modo que sea de utilidad para [Smart&Printing3D](https://instagram.com/smartprinting3d?igshid=lnryp1lool4m). Este estimado se lleva a cabo teniendo en cuenta una serie de parámetros sobre el material, la maquina y la mano de obra.
Este proyecto se realiza a modo de aprendizaje sobre el desarrollo de una aplicación básica en Python mediante la librería para interfaz grafica [Tkinter](https://docs.python.org/es/3.8/library/tk.html).


## Comenzando

### Ambiente de desarrollo.

Para el ambiente de desarrollo, solo es necesario tener instalados los siguientes módulos.
- Python 3.8
- [Tkinter](https://docs.python.org/es/3.8/library/tk.html)
- [configparser](https://docs.python.org/3.8/library/configparser.html)
- [pyinstaller](https://pypi.org/project/pyinstaller/)

Posteriormente se clona el repositorio:

```
git clone https://github.com/Sistemas-Inteligentes-en-Red/isa-arpex-server.git
```

Este repositorio cuenta con dos ramas, de las cuales dev es la rama a la cual se suben los cambios en desarrollo.

### Instalación.

Una vez empaquetada la aplicación mediante PyInstaller, esta se vuelve un ejecutable y no es necesario instalarla.

## Ejecución de pruebas

Para realizar la prueba de funciones del backend, es necesario ejecutar el script test_calculatorcore.py que se encuentra dentro de la carpeta [test](https://github.com/MateoVelasquez/3Dprinter_calculator/tree/main/test).
Es importante ejecutar este script con la consola ubicada en la carpet /test con el comando:

```
python test_calculatorcore.py
```
Este script ejecuta pruebas a las dos funciones principales, las cuales son la modificación del archivo ini de configuración y la prueba de calculo.
Si ambas pruebas son correctas, el resultado impreso en consola será:

```
PRUEBA DE MODIFICACION INI:  Correcto
PRUEBA DE CALCULO:  Correcto
```

## Generación del ejecutable.

Para generar el ejecutable .exe de la aplicación, es necesario primero limpiar las carpetas build y dist en caso de que existan, para evitar un posible conflicto.
Si se está haciendo uso de Anaconda, debe activarse el ambiente de desarrollo que contiene las dependencias necesarias.
Posteriormente se ejecuta, mediante PyInstaller, el archivo setup.spec que se encuentra en el directorio principal del repositorio, tal como se muestra a continuación.

```
pyinstall setup.spec
```
De esta manera, se regeneran las carpetas build y dist, siendo esta ultima la que contiene el ejecutable 3D_cost_calculator.exe


## Versiones

Actualmente esta aplicación se encuentra en su versión de pruebas Alpha. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/MateoVelasquez/3Dprinter_calculator/tags).

## Autores ✒️

* **Mateo Velásquez** - *Trabajo Inicial* - [MateoVelasquez](https://github.com/MateoVelasquez)

## Licencia 📄

Este proyecto está bajo la Licencia (Creative Commons by-nc-sa 4.0) - mira el archivo [LICENSE.md](LICENSE.md) para más detalles

## Expresiones de Gratitud 🎁

* Agradecimientos a Margarita R. Velásquez quien se encarga de probar la aplicación en busca de fallas y bugs.
