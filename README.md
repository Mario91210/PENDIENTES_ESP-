# PENDIENTES_ESP-

Mario Humberto Gonzalez 

mario.gonzalez21.mgd@gmail.com

Campus Coquimatlán, 28400

"Facultad de Ingeniería Civil, PE-ITG..." Programa educativo Ingeniero Topografo Geomatico"

#	LECTURA DE DATOS DE PENDIENTES DESDE EXCEL PARA LA AGRICULTURA DEL EJIDO LA ESPERANZA

Muestra los datos obtenidos de obtención de las pendientes del Ejido la Esperanza y finalmente poder mostrar una imagen de dicho Ejido.

![PalabrasdelTextoAlternativo](https://github.com/Mario91210/PENDIENTES_ESP-/blob/master/IMAGENES/mapa.png)


En la siguiente Imagen se muestra una pequeña simbologia del los rangos de elevacion con sus respectivos colores

![PalabrasdelTextoAlternativo](https://github.com/Mario91210/PENDIENTES_ESP-/blob/master/IMAGENES/100824229_254689352259777_1170690346951114752_n.png)

Las pendientes que son aptas para poder establacer agricultura son los que tienen color verde en el mapa que se muestra anteriormente, las cuales son las que tienen una pendiente apta para esto, dichas pendietnes tienen una inclinación de 0 grados hasta 5 grados de inclinación.

# RESUMEN
En el presente proyecto se preverá in-formación sobre un ejido, específica-mente del ejido la esperanza, del cual se obtendrán características de las pendientes que tiene el ejido, esto se realiza con la finalidad de poder mostrar pendientes aptas para la agricultura.
Palabras clave: Sembrar, Cultivo, Mapa Temático, Pendiente

# ABSTRACT 
In this project will provide for in-formation on an ejido, specific-minded of the ejido hope, from which will obtain characteristics of the slopes that the ejido has, this is done in order to be able to show slopes suitable for agricul-ture.
Keywords: Agriculture, Cultivation, Slopes

# INTRODUCCIÔN 
En el presente proyecto se mostrarán los resultados obtenidos de la elaboración de un ráster de elevaciones, elaborado en un sis-tema de información geográfica, específica-mente ArcGIS, el ráster de elevaciones se obtiene mediante datos vectoriales propor-cionados por el INEGI mediante su página web.
La elaboración del presente trabajo tiene como objetivo poder mostrar las pendientes que son aptas para poder hacer practica de la agricultura, lo cual se realiza mediante daros vectoriales.
El proyecto esta compuesto principalmente por el desarrollo de un programa en Python, con el programa se pretende facilitar la ob-tención del conocimiento sobre las pendien-tes del ejido la esperanza, por lo que se sis-tematiza la obtención de la superficie de las diferentes pendientes que tiene el ejido la esperanza clasificándolos por colores para cada una de las pendientes que va desde 5° hasta los 64°, tomando en cuenta que las pendientes aptas para la agricultura son las menores de 5° y en algunos casos menores de 10°.

# DESARROLLO
Para desarrollar este programa se tiene que utilizar un paquete de Python que proporciona los diferentes pendientes que tiene el ejido a estudiar con la herramienta de los sistemas de información Geográfica como lo es ArcGis

1.- Se tiene que importar e instalar la librería usada la cual es "openpyxl" ya que con ella se basara nuestro proyecto.

2.- Para poder leer el programa se tiene que tener el ejido a estudiar como shp para que con ese formato podamos sacar las características de las pendientes.

3.- Se toman y verifican las características del terreno a estudiar para poder tener los cálculos necesarios

4.- Se imprimen los datos correspondientes para poder correr el programa.

5.-Se especifica lo que se tiene que imprimir mediante la tabla de atributos del ejido.

6.- Al poner la condición en el programa en Python se denominará dependiendo de los grados el cultivo para lo cual es buena esa área, ya sea agrícola o de agricultura.

7.- Se espera que el mapa a realizar junto con el programa señale con diferentes colores las diferentes pendientes las cuales puedan ser de buena utilidad.

# MANEJO DE DATOS
El tipo de datos que se manejan en el programa son:

Datos geoespaciales: son requeridos para la localización de las curvas de nivel del ejido y el sistema de referenciación.

Lenguaje de programación: para lograr crear el programa y este ejecute correctamente lo que se pide.

Sistemas de Información Geográfica: los SIG importantes para el desarrollo de la localización de cada zona apta para el cultivo.
1.1. Sistema Operativo El programa está diseñado para trabajar en el Sistema Operativo Windows.
1.2. Equipo de prueba El equipo en el cual fue probado el programa es una computadora portátil de la marca Hp pavilion Gaming con las siguientes características:

![PalabrasdelTextoAlternativo](https://github.com/Mario91210/PENDIENTES_ESP-/blob/master/IMAGENES/Manejo1.png)

# RESULTADOS
Lo que se logró obtener con el código fue un programa en el cual se extraen desde uns archivo xlsx los diferentes ángulos de las pendientes que tiene nuestro ejido para obtener las pendientes que son recomendables a este tipo de casos y que se pueda usar en ámbito de la agricultura.

En el siguiente código se producen desde el Angulo mínimo hasta el ángulo máximo

![PalabrasdelTextoAlternativo](https://github.com/Mario91210/PENDIENTES_ESP-/blob/master/IMAGENES/RESULTADOS.png)

Con la tabla mostrada anteriormente, generamos unas graficas en la que se pudem observar las diferentes pendientes que existen en el Ejido la Esperanza

![PalabrasdelTextoAlternativo](https://github.com/Mario91210/PENDIENTES_ESP-/blob/master/IMAGENES/Grafica1.png)

![PalabrasdelTextoAlternativo](https://github.com/Mario91210/PENDIENTES_ESP-/blob/master/IMAGENES/Grafica2.png)

El código completo se anexa en el si-guiente párrafo

import openpyxl

import PIL

importar pandas

importar  matpltlib

workbook = "proyectoespecial.xlsx"

df = pd.read_excel(workbook)

print(df.head())

valores = df[["Pendiente","Porcentaje"]]

print(valores)

ax = valores.plot.bar(x = "Pendiente", y = "Porcentaje", rot = 0)

plt.show()
    
Si desea ver la imagen del area de estudio indique "y"

run = raw_input("Desea ver el Ejido de estudio y/n\n")

from PIL import Image

Para que la imagen pudea ser mostradra debera de indicarse con el nombre de la imagen

def show(path_name):

    image = ()

image.open(path_name)=

    image.show()

show()

# CONCLUSIÒN
Durante la elaboración del proyecto se pudo observar que es bastante impor-tante la comprensión de las librerías dentro de Python tanto como la com-prensión de Python debido a que, si no se comprende bien alguno de estos te-mas, se tendrán dificultades para poder trabajar dentro de ellos debido a que las librerías se dividen en diferentes partes.
Durante la elaboración del código se tuvieron algunos percances debido a que no se tenían contempladas la libre-rías que se utilizarían para poder elabo-rar correctamente el código del progra-ma, por lo que se tuvieron que analizar y comprender diferentes librerías para poder trabajar correctamente, por lo que se decidió trabajar con las librerías de openpyxl  y PIL.

# REFERENCIAS 
https://www.inegi.org.mx/app/mapas/

https://www.arcgis.com)

POSTER DE REPRESENTACION DEL PROYECTO

![PalabrasdelTextoAlternativo](https://github.com/Mario91210/PENDIENTES_ESP-/blob/master/IMAGENES/poster1.jpg)



