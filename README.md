<div align="justify">

<div align="center">
  <img src="https://www.unipython.com/wp-content/uploads/2017/07/pygame_logo.gif" width="500px" />
</div>

## Introducción

  El presente repositorio tiene como objetivo la descripción básica de __pygame__. Se centrará en la preparación del entorno y la creación de ejemplos básicos.

## ¿Qué es?

  Lo primero que hay que __pygame__ es una biblioteca multimedia (que trabaja sobre las librerías SDL) que permiten la creación de _videojuegos en dos dimensiones de una manera sencilla_.

  Usando __pygame__ vamos a programar algunos videojuegos. __No__ realizaremos un juego inmenso __en 3D__ con gráficas espectaculares y que necesite equipos potentes para ser usado. Mas bien lo que vamos a obtener son juegos en 2D similares a los de _consolas como supernintendo, portátiles como el GBA, nintendoDS (sin la parte táctil), etc_.

## Requisitos

- Tener instalado python y _pygame_. Ambas están disponibles para varios sistemas (como Windows, GNU/Linux, Mac, etc.) así que los juegos creados serán multiplataforma.
- Conocimiento básico de python, por lo menos como se definen funciones y clases
- Conocimientos básicos de matemáticas y física, lo que resulta útil al programar juegos en general. Básicamente es algo de física clásica como los conceptos de velocidad, aceleración, etc. y de matemáticas como los conceptos de puntos, coordenadas en el espacio, etc.

## Instalación

### Instalación de Pip en Ubuntu

  _Nos centraremos en el trabajo de instalación y desarrollo en Linux, concretamente en Ubuntu_.

#### Instalación de Pip para Python 3

  Si queremos instalar __pip__ para _Python 3 en Ubuntu 20.04_, no tendremos más que ejecutar los siguientes comandos en una terminal (Ctrl+Alt+T):  

  ```console
    sudo apt update && sudo apt install python3-pip
  ```

  El anterior comando también va a instalar todas las dependencias necesarias para construir módulos de Python.

  Cuando se complete la instalación, podremos verificar la instalación y comprobar la versión instalada ejecutando el comando:

  ```console
    pip3 --version
  ```

  _El número de versión puede variar, pero se verá más o menos como se puede ver en la anterior captura de pantalla_.

  ```console
    pip 20.3.3 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)
  ```

#### Algunos conceptos básicos para utilizar Pip

  Ahora vamos a ver algunos comandos básicos útiles de pip. Con esta herramienta podremos instalar paquetes desde PyPI, control de versiones, proyectos locales y desde archivos de distribución.

  Para ver la lista de todos los comandos y opciones disponibles solo habrá que escribir:

  ```console
    pip3 --help
  ```

  Podremos obtener más información sobre un comando específico usando el comando pip –help. Por ejemplo, para obtener más información sobre el comando de instalación, no hay más que escribir:

  ```console
      pip3 install --help
  ```

#### Instalar paquetes con Pip

  Supongamos que nos interesa instalar un paquete llamado scrapy, que se utiliza para extraer datos de sitios web. Para instalar la última versión del paquete, no hay más que ejecutar el comando:

  ```console
    pip3 install scrapy
  ```

  Para instalar una versión específica del paquete, tan solo tendremos que añadir == y el número de versión después del nombre del paquete:

  ```console
    pip3 install scrapy==1.5
  ```

  _Podríamos reemplazar pip3 con pip2 si utilizamos Python 2_.

  Actualizar un paquete
  Para actualizar un paquete ya instalado a la última versión, el comando a utilizar será algo como lo siguiente:

  ```console
      pip3 install --upgrade nombre_paquete
  ```

#### Instalar paquetes utilizando un archivo de requisitos

  Si disponemos de un archivo de texto que contiene una lista de paquetes pip con sus versiones necesarias para ejecutar un proyecto específico de Python. Vamos a poder utilizar el siguiente comando para instalar la lista de requisitos especificados ese archivo:

  ```console
      pip3 install -r requirements.txt
  ```

#### Listar paquetes instalados

  Para enumerar todos los paquetes pip instalados, no hay más que instalar el siguiente comando:

  ```console
    pip3 list
  ```

#### Desinstalar paquetes

  Para desinstalar un paquete, no hay más que ejecutar algo como:

  ```console
    pip3 uninstall nombre_paquete
  ```

## Primeros pasos  

  Lo primero hay que hay que hacer es importar el modulo de pygame, lo cual se hace simplemente como:

  ```console
    import pygame
    from pygame.locals import *
  ```

  La segunda linea es opcional (pero muy recomendada), ya se utiliza para importar una serie de constantes que tiene pygame (como las teclas del teclado).

  Ahora en general nuestro código en pygame tendrá una estructura como esta:

  ```console
  #!/usr/bin/env python
  # -*- coding: utf-8 -*-

  # Importacion de los módulos
  import pygame
  from pygame.locals import *
  # y cualquier otro modulo usado

  # ----------------------------------------------
  # Constantes, como anchos y largo de pantalla, etc.
  # ----------------------------------------------

  # ----------------------------------------------
  # Clases y Funciones utilizadas (lo explicare en la siguiente parte)
  # ----------------------------------------------

  def main():
    pygame.init()
    # La clase o función principal que crea o ejecuta el juego
    # Contiene principalmente loop del juego (el alma de este)

  if __name__ == "__main__":
    main()
  ```

  Si te fijas en la linea 18 se hace un __pygame.init()__, esto es para que se inicie pygame y es necesario ejecutarlo antes de empezar a usar pygame (por eso fue incluido al inicio de la función principal del juego). Si no te gusta incluir el pygame.init() en la función del juego, otro buen lugar es incluirlo inmediatamente después del if __name__ == "__main__": (antes de llamar a la función main()).

## Referencias

- [Instalación](https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation).
- [ejemplos-basicos](ejemplos-basicos).
<!--
- []().
- []().
-->
</div>
