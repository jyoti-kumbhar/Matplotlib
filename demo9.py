import random
import pandas as pd
from matplotlib import pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation

x=[]
y=[]
index = count()
def animate(i):
    x.append(next(index))
    y.append(random.randint(0,5))
    plt.cla()
    plt.plot(x,y)
ani = FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)

plt.tight_layout()
plt.show()
