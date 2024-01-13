from numpy import array
from PIL import Image
import colorsys
import os
setWidth = 1000

# Prevent bugs on UNIX-based systems
if os.name == 'posix':
    os.system('clear')
else:
    os.system('cls')

# The value of the constant c = x + yi is initialized to 0
cxValue = 0
cyValue = 0
cValue = 0

# Get user input to determine whether to plot the Mandelbrot set or a Julia set
value = input("Generate Mandelbrot set or Julia set? (input \"M\" for Mandelbrot and \"J\" for Julia) ")
if value in "Mm":
    toDraw = 0
elif value in "Jj":
    toDraw = 1

    # When Julia set is selected, get the real and imaginary components of c
    cxValue = input("\nWhat is the real part of c? ")
    cyValue = input("\nWhat is the imaginary part of c (without the i)? ")
    cxValue = float(cxValue)
    cyValue = float(cyValue)

# Sets the color scheme for the plot
def color(n):
    setColor = 255 * array(colorsys.hsv_to_rgb(n / 80, 100.0, 66.0))
    return tuple(setColor.astype(int))

# Computes the Mandelbrot set and corresponding colors
def mandelbrot(x, y):
    c = complex(x, y)
    z = 0
    for n in range(1, 1000):
        if abs(z) > 2:
            return color(n)
        z = z * z + c
    return (0, 0, 0)

# Computes the Julia set and corresponding colors
def julia(x, y):
    c = complex(cxValue, cyValue)
    z = complex(x, y)
    for n in range(1, 1000):
        if abs(z - c) > 2:
            return color(n)
        z = z * z + c
    return (0, 0, 0)

# Generate the image
image = Image.new('RGB', (setWidth, setWidth // 2))
pixels = image.load()
if toDraw == 0:
    for x in range(image.size[0]):
        print("%.2f %%" % (x / setWidth * 100.0))
        for y in range(image.size[1]):
            pixels[x, y] = mandelbrot((x - (0.75 * setWidth)) / (setWidth / 4), (y - (setWidth / 4)) / (setWidth / 4))
elif toDraw == 1:
    for x in range(image.size[0]):
        print("%.2f %%" % (x / setWidth * 100.0))
        for y in range(image.size[1]):
            pixels[x, y] = julia((x - (0.5 * setWidth)) / (setWidth / 4), (y - (setWidth / 4)) / (setWidth / 4))

# Plot the image
image.show()
