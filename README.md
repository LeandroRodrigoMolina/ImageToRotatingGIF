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
