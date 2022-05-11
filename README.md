# Proyecto 3
Alumno: Alberto Espinosa Juárez

Programa Académico: Maestría en Ciencias de la Computación

## ¿Qué contiene el proyecto 3?
El proyecto 2 consiste en utilizar la biblioteca creada en "Proyecto_01" para implementar el algoritmo de Dijkstra.

Utilizando la biblioteca de grafos desarrollada en el proyecto 1, implementar el algoritmo de Dijkstra de tal forma que dado un nodo fuente (s), calcule el árbol de caminos más cortos; es decir, desarrollar el método en la clase Grafo:

- def Dijkstra(self, s):


Los archivos que contiene la carpeta "Proyecto_03" son: 
+ nodo.py Archivo que contiene la clase que define a un nodo y sus métodos
+ arista.py Archivo que contiene la clase que define a una arista y sus métodos
+ grafo.py y archivos para cada algoritmo. Archivos que contienen la clase que define a un grafo y sus métodos, además, contiene los algortimos descritos para el proyecto 1 y contiene los algoritmos DFS (recursivo e iterativo) y BFS, correspondientes al proyecto 02, así como Dijkstra para el proyecto03.
+ main.py Archivo que contiene la generación y guardado de cada uno de los grafos, tanto los generados como los calculados.
+ Carpeta gv que contiene por subcarpetas los algortimos con sus correspondientes archivos .gv e imágenes
+ ADA_Proyecto3.ipynb este archivo es un notebook en caso de quererlo replicar en Notebook

## Ejecución en local y en nube (Colab)
Para este proyecto realicé dos versiones
1. Ejecución en nube utilizando Google Colab. Para ejecutar el código se debe ir a la siguiente liga https://colab.research.google.com/drive/1aOP992VaRhQmEQBGlUawPwWniKHR2xEu?usp=sharing y ejecutar todas las celdas (iniciando de arriba para abajo). No debería existir problema alguno. Los grafos generados se guardan en la sección de "files" dentro de Google Colab (icono de folder en el menú izquierdo).
2. Ejecución en local. Si se clona el repositorio se puede ejecutar en local. Solo se pide leer antes el archivo grafo2dot pues es importante (solo en local).

## ¿Cómo veo la documentación?
Para revisar la documentación es necesario hacer uso del método *help(método)* que nos brindará información sobre cómo y qué hace un método.

**Ejemplo**

help(guardar_grafo)

**Desplegará información sobre el método guardar_grafo así como también de los parámetros que recibe**

## Resúmen del proyecto 3

### Modelo de malla de pocos nodos
#### Generado
![Grafo en malla de pocos nodos][malla1]
#### Calculado con Dijkstra
![Grafo en malla calculado con pocos nodos][malla2]

[malla1]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/Malla/Malla_3_3.png
[malla2]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/Malla/Malla_3_3_Dijkstra.png


### Modelo de malla de muchos nodos
#### Generado
![Grafo en malla de muchos nodos][malla100]
#### Calculado con Dijkstra
![Grafo en malla calculado con BFS][malla1002]


[malla100]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/Malla/Malla_25_4.png
[malla1002]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/Malla/Malla_25_4_Dijkstra.png


### Modelo Erdos y Renyi de pocos nodos

#### Generado
![Grafo erdos renyi 30 nodos y 400 aristas][erdos1]
#### Calculado con Dijkstra
![Grafo erdos renyi calculado con Dijkstra][erdos2]


[erdos1]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/ErdosRenyi/ErdosRenyi_20_30.png
[erdos2]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/ErdosRenyi/ErdosRenyi_20_30_Dijkstra.png


### Modelo Erdos y Renyi de muchos nodos

#### Generado
![Grafo erdos renyi 100 nodos y 1500 aristas][erdos100]
#### Calculado con Dijkstra
![Grafo erdos renyi calculado con Dijkstra][erdos1002]


[erdos100]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/ErdosRenyi/ErdosRenyi_100_100.png
[erdos1002]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/ErdosRenyi/ErdosRenyi_100_100_Dijkstra.png


### Modelo Gilbert pocos nodos
#### Generado
![Gilbert 30 nodos][gilbert1]
#### Calculado con Dijkstra
![Gilbert calculado con Dijkstra][gilbert2]


[gilbert1]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/Gilbert/Gilbert_30_10.png
[gilbert2]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/Gilbert/Gilbert_30_10_Dijkstra.png


### Modelo Gilbert de muchos nodos
#### Generado
![Gilbert 100 nodos][gilbert100]
#### Calculado con Dijkstra
![Gilbert calculado con Dijkstra][gilbert1002]


[gilbert100]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/Gilbert/Gilbert_100_10.png
[gilbert1002]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/Gilbert/Gilbert_100_10_Dijkstra.png



### Modelo geográfico de pocos nodos
#### Generado
![geografico 30 nodos][geo1]
#### Calculado con Dijkstra
![geografico calculado con Dijkstra][geo2]


[geo1]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/Geografico/Geografico_30_3.png
[geo2]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/Geografico/Geografico_30_3_Dijkstra.png


### Modelo geográfico de muchos nodos
#### Generado
![geografico 100 nodos][geo100]
#### Calculado con Dijkstra
![geografico calculado con Dijkstra][geo1002]


[geo100]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/Geografico/Geografico_100_3.png
[geo1002]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/Geografico/Geografico_100_3_Dijkstra.png


### Modelo Barabási-Albert de pocos nodos
#### Generado
![albert 30 nodos][albert1]
#### Calculado con Dijkstra
![albert calculado con Dijkstra][albert2]


[albert1]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/BabarasiAlbert/BarabasiAlbert_30_4.png
[albert2]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/BabarasiAlbert/BarabasiAlbert_30_4_Dijkstra.png


### Modelo Barabási-Albert de muchos nodos
#### Generado
![albert 100 nodos][albert100]
#### Calculado con Dijkstra
![albert calculado con Dijkstra][albert1002]


[albert100]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/BabarasiAlbert/BarabasiAlbert_100_4.png
[albert1002]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/BabarasiAlbert/BarabasiAlbert_100_4_Dijkstra.png



### Modelo Dorogovtsev-Mendes de pocos nodos
#### Generado
![Dorogovtsev-Mendes 30 nodos][mendes1]
#### Calculado con Dijkstra
![Dorogovtsev-Mendes calculado con Dijkstra][mendes2]


[mendes1]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/DorogovtsevMendes/DorogovtsevMendes_30.png
[mendes2]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/DorogovtsevMendes/DorogovtsevMendes_30_Dijkstra.png

### Modelo Dorogovtsev-Mendes de muchos nodos
#### Generado
![Dorogovtsev-Mendes 100 nodos][mendes100]
#### Calculado con Dijkstra
![Dorogovtsev-Mendes calculado con Dijkstra][mendes1002]


[mendes100]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/DorogovtsevMendes/DorogovtsevMendes_100.png
[mendes1002]: https://github.com/AlbertoEJ/ADA3/blob/main/Proyecto03/gv/DorogovtsevMendes/DorogovtsevMendes_30_Dijkstra.png



