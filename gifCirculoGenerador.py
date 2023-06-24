from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw
import numpy as np
import imageio

try:
    # Inicia la interfaz de Tkinter
    Tk().withdraw()

    # Abre el diálogo para seleccionar archivo y guarda el nombre del archivo
    filename = askopenfilename(filetypes = [("Image files", "*.png *.jpg *.jpeg *.tiff *.bmp")])

    # Carga la imagen
    try:
        img = Image.open(filename)
    except IOError:
        print("No se puede abrir la imagen. Asegúrate de que el archivo es una imagen y está en el lugar correcto.")
        exit()

    # Asegúrate de que la imagen sea cuadrada para que quede bien después de la rotación
    img = img.resize((min(img.size),)*2).convert('RGBA')

    # Hacer un círculo
    bigsize = (img.size[0] * 3, img.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(img.size, Image.ANTIALIAS)
    img.putalpha(mask)

    # Crear imágenes rotadas y guardar en una lista
    imgs = []
    for i in range(360):  # Ahora crea 360 cuadros
        rotated = img.rotate(i)  # 1 grado de rotación por cuadro para 360 cuadros = 360 grados
        imgs.append(rotated)

    # Guardar las imágenes como un GIF
    try:
        imageio.mimsave('miImagen.gif', imgs, 'GIF', duration = 0.011111)  # Cada cuadro se muestra durante 0.011111 segundos
    except IOError:
        print("No se puede guardar la imagen. Asegúrate de que tienes los permisos necesarios y que hay suficiente espacio en el disco.")
except Exception as e:
    print(f"Se produjo un error inesperado: {str(e)}")
