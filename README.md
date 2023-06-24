# Generador de gif en forma circular en movimiento
Este programa toma una imagen de entrada seleccionada por el usuario y la convierte en un GIF animado. La imagen se gira 360 grados, con cada grado de rotación formando un cuadro en el GIF final. La imagen de entrada se recorta en un círculo y se aplica un efecto de rotación para lograr el efecto deseado.

## Requisitos previos

### Dependencias

Este programa requiere las siguientes bibliotecas de Python:

1. **Tkinter**: Para proporcionar la interfaz gráfica de usuario que permite a los usuarios seleccionar archivos.
2. **Pillow (PIL)**: Para manejar las operaciones de imagen.
3. **NumPy**: Para el manejo de operaciones matemáticas en matrices multidimensionales.
4. **imageio**: Para escribir las imágenes rotadas como un archivo GIF.

### Instalación de dependencias

#### En Windows:

Para instalar las dependencias requeridas en Windows, primero debe tener Python instalado en su sistema. Asegúrese de que Python esté en su PATH. Luego, puede instalar las bibliotecas requeridas usando `pip` (el administrador de paquetes de Python) a través de la línea de comandos:

```sh
pip install tkinter pillow numpy imageio
```

#### En Linux:

Para instalar las dependencias requeridas en Linux, también necesita tener Python instalado en su sistema. En la mayoría de las distribuciones de Linux, Python ya está preinstalado. Puede usar `pip` para instalar las bibliotecas requeridas:

```sh
pip install tkinter pillow numpy imageio
```

Si `pip` no está instalado, puede instalarlo con:

```sh
sudo apt-get install python3-pip
```

Para Tkinter, es posible que necesite instalarlo con el administrador de paquetes de su distribución. Por ejemplo, en Ubuntu, puede hacerlo con:

```sh
sudo apt-get install python3-tk
```

## Uso

Después de instalar las dependencias requeridas, simplemente ejecute el script en Python. Aparecerá una ventana de diálogo que le pedirá que seleccione una imagen. Después de seleccionar la imagen, el programa creará un GIF rotativo a partir de la imagen y lo guardará como 'miImagen.gif' en el mismo directorio en el que se ejecuta el script.

## Ajustar la velocidad del GIF

Si deseas aumentar la velocidad del GIF generado, puedes hacerlo con la ayuda de herramientas en línea, como [EZGIF.com](https://ezgif.com/speed). EZGIF es una plataforma en línea gratuita que ofrece una variedad de herramientas de edición de GIF. Sigue los pasos a continuación para ajustar la velocidad de tu GIF:

1. Ve a [https://ezgif.com/speed](https://ezgif.com/speed).
2. Haz clic en "Seleccionar archivo" y elige el GIF que quieras acelerar.
3. Haz clic en "Subir" para cargar tu GIF.
4. Después de que se haya cargado el archivo, puedes ver una opción para cambiar la velocidad de tu GIF. Ingresa un porcentaje mayor al 100% para aumentar la velocidad del GIF.
5. Haz clic en "Cambiar la velocidad del GIF" para aplicar los cambios.
6. Finalmente, puedes descargar el GIF más rápido haciendo clic en "Guardar".

Por favor, ten en cuenta que al aumentar la velocidad del GIF, estás aumentando la cantidad de fotogramas que se muestran por segundo, lo que puede hacer que el GIF parezca más corto.
