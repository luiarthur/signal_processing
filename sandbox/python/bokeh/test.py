import numpy as np

from bokeh.plotting import figure, show, output_file

N = 500
x = np.linspace(0, 10, N)
y = np.linspace(0, 10, N*2)
xx, yy = np.meshgrid(x, y)
d = np.sin(xx)*np.cos(yy)

p = figure(x_range=(0, 10), y_range=(0, 20))

# must give a vector of image data for image parameter
p.image(image=[d], x=0, y=0, dw=10, dh=20, palette="Spectral11")

output_file("html/image.html", title="image.py example")

show(p)  # open a browser
