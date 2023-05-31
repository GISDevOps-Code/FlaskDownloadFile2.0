from pylab import imshow, show, get_cmap
from numpy import random
import matplotlib.pyplot as plt
from datetime import datetime

def CreateImage(Name, Height, Width, Color, Style):
    Z = random.random((Height,Width))   # Test data

    imshow(Z, cmap=get_cmap(Color), interpolation=Style)
    now = datetime.now()
    date = now.strftime("%m%d%Y%H%M%S")
    fileName = "downloads" + "\\" + Name + "_" + date +".png"
    plt.savefig(fileName)
    show()
    plt.close()
