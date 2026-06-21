import numpy as np 
import matplotlib.pyplot as plt


# Normalized angular coordinates (units of theta_E)
xc = 0.5
yc = 0.2
R = 0.05
n = 300
theta_e = 1.0

def get_images(beta, e):
    return (beta + np.sqrt(beta**2 + 4*e**2))/2, (beta - np.sqrt(beta**2 + 4*e**2))/2

# Sampling points in source circle
phi = 2*np.pi*np.random.rand(n)
r = R*np.sqrt(np.random.rand(n))
xs = xc + r*np.cos(phi)
ys = yc + r*np.sin(phi)

beta = np.sqrt(xs**2 + ys**2)
out1, out2 = get_images(beta, theta_e)

ux = xs / beta
uy = ys / beta

# Image 1 (outer)
img1_x = out1 * ux
img1_y = out1 * uy

# Image 2 (inner)
img2_x = out2 * ux
img2_y = out2 * uy

plt.style.use('seaborn-v0_8-darkgrid')
plt.figure(figsize=(8, 8))

plt.scatter(xs, ys, s=5, color="royalblue", label="Source")
plt.scatter(img1_x, img1_y, s=5, color="firebrick", label="Image 1")
plt.scatter(img2_x, img2_y, s=5, color="forestgreen", label="Image 2")
plt.scatter(0, 0, s=100, color='black', marker='o', label='Lens')

plt.gca().set_aspect('equal')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlabel(r'$\theta_x / \theta_E$')
plt.ylabel(r'$\theta_y / \theta_E$')
plt.title('Lensing of an Extended Source')

plt.show()