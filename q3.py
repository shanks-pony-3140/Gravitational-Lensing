import numpy as np 
import matplotlib.pyplot as plt


# Constants
G = 6.67430e-11
M = 1.989e30  # 1 solar mass
c = 3e8
dl = 5e11
ds = 9.75e17
dls = ds - dl

# Source position (side view coordinates)
xs = 5e16
ys = ds

def approx_theta(beta, theta_e):
    return (beta + np.sqrt(beta**2 + 4*theta_e**2))/2, (beta - np.sqrt(beta**2 + 4*theta_e**2))/2

# Einstein angle
theta_e = np.sqrt((4*G*M/c**2) * (dls/(dl*ds)))

beta = xs / ys
out1, out2 = approx_theta(beta, theta_e)

# Image positions
x1 = out1 * ys
x2 = out2 * ys

plt.style.use('seaborn-v0_8-darkgrid')
plt.figure(figsize=(10, 6))

plt.scatter(0, 0, s=100, color='black', marker='x', label='Lens')
plt.scatter(xs, ys, s=50, color='blue', label='Source')
plt.scatter(0, -dl, s=50, color='purple', label='Observer')
plt.scatter(x1, ys, s=50, color='red', label='Image 1')
plt.scatter(x2, ys, s=50, color='orange', label='Image 2')

plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1, alpha=0.3)

plt.xlabel('Transverse distance (m)')
plt.ylabel('Distance along optical axis (m)')
plt.title('Point Mass Gravitational Lensing (Side View)')
plt.legend()
plt.grid(True)
plt.show()