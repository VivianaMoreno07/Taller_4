import numpy as np
#Tenemos que importar matplotlib, que es una biblioteca especializada mas que todo en graficos
import matplotlib.pyplot as plt
#Se define la funcion Matplotlib con las tres variables que se van a trabajar en el codigo
def mandelbrot(h, w, maxit=20, r=2):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    x = np.linspace(-2.5, 1.5, 4*h+1) # Se crea un rango de numeros entre -2.5 y 1.5 y con eso se crea una lista con el espacio definido 
    y = np.linspace(-1.5, 1.5, 3*w+1)
    A, B = np.meshgrid(x, y)
    C = A + B*1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r                   
        div_now = diverge & (divtime == maxit)  
        divtime[div_now] = i                    
        z[diverge] = r                          

    return divtime
plt.clf()
plt.imshow(mandelbrot(400, 400))