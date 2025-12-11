#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import pi,sin
import numpy as np
v=3*(10**8)
f= 50 
w=1
k=1
E=1
B=1

#punt del espai
def wave_point(A,t, x_vals):
    return A*np.sin(k*x_vals -w*t)

def gen_wave(n_frames, n_x, dt):
    time_points=[]
    x_vals= np.linspace(0, 4*np.pi, n_x)
    for i in range(0, n_frames):
        t = i * dt
        time_points.append(list(zip(x_vals, wave_point(E,t,x_vals),wave_point(B,t,x_vals+np.pi/2))))

    return time_points


# In[2]:


mostra=gen_wave(100, 100,0.1)


# In[3]:


print(mostra)


# In[4]:


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D  # noqa
from IPython.display import HTML
from matplotlib import rc

# Muy importante: decirle a matplotlib que use HTML con JS
rc('animation', html='jshtml')

# -----------------------
# 1. Tus datos
# -----------------------
# frames = [...]
frames=mostra
# -----------------------
# 2. Figura 3D
# -----------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# lineas vacias al inicio
lineaE,= ax.plot([], [], [], label='Campo eléctrico E')
lineaB,= ax.plot([], [], [], label='Campo magnético B')

ax.set_xlabel("x (propagación)")
ax.set_ylabel("Intensidad Y (E)")
ax.set_zlabel("Intensidad Z (B)")

# limites (ajusta si quieres)
ax.set_xlim(0, 4*np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.legend()

# -----------------------
# 3. Función de actualización
# -----------------------
def update(i):
    frame = frames[i]
    x = [p[0] for p in frame]
    y = [p[1] for p in frame]
    z = [p[2] for p in frame]

    # Línea del campo eléctrico: (x, Ey, 0)
    lineaE.set_data(x, y)
    lineaE.set_3d_properties([0.0]*len(x))
    # Línea del campo magnético: (x, 0, Bz)
    lineaB.set_data(x, [0.0]*len(x))
    lineaB.set_3d_properties(z)
    return lineaE, lineaB

ani = FuncAnimation(fig, update, frames=len(frames), interval=50, blit=False)

# -----------------------
# 4. Mostrar animación EN JUPYTER
# -----------------------
HTML(ani.to_jshtml())


# In[5]:


frames


# In[6]:


mostra


# In[7]:


with open("frames.txt", "w", encoding="utf-8") as f:
    f.write(str(frames))


# In[8]:


with open("mostra.txt", "w", encoding="utf-8") as f:
    f.write(str(mostra))


# In[9]:


ani.save("onda.gif", writer="pillow", fps=20)


# In[10]:


ani.save("onda.mp4", fps=30, dpi=150)

