import numpy as np
import matplotlib.pyplot as plt


f=1

x_in = input("enter the x-coord (default -2.0): ")
y_in = input("enter the y-coord (default 0.5): ")

x = float(x_in) if x_in else -2.0
y = float(y_in) if y_in else 0.5
def valid(x,y):
    if abs(y)<=1.5:
        if abs(x)==f:
            v=999
        else: 
            v=1/((1/x)+(1/f))
        m=y*(v/x)
        return v,m
    else:
        print("invalid y coordinate: lens height is from -1.5 to 1.5")
        return None,None

v,m=valid(x,y)

plt.style.use('seaborn-v0_8-darkgrid')
x1vals=np.linspace(x, 0,100)
y1vals=y*np.ones(len(x1vals))

x2vals=np.linspace(0, v,100)
y2vals=np.linspace(y, m,100)

plt.plot(x,y,'bo',label='Object')
plt.plot(v,m,'ro',label='Image')
plt.plot(x1vals,y1vals,label='Incident ray')
plt.plot(x2vals,y2vals,label='Refracted ray')

plt.axvline(0, color='black', linestyle='--', label='Lens')
plt.axhline(0, color='black', linewidth=1)

xmin=min(x,v)-1
xmax=max(x,v)+1

ymin=min(y,m)-1
ymax=max(y,m)+1

plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.show()

    
    
