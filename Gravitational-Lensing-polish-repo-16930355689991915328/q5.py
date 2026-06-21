import numpy as np 
import matplotlib.pyplot as plt


# Sequence of source transverse positions (normalized)
beta_vals = [1.5, 1.0, 0.5, 0.1, 0.0]
theta_e = 1.0

plt.style.use('seaborn-v0_8-darkgrid')

for b in beta_vals:
    plt.figure(figsize=(6, 6))
    
    if b > 0:
        # Two image points
        t1 = (b + np.sqrt(b**2 + 4*theta_e**2))/2
        t2 = (b - np.sqrt(b**2 + 4*theta_e**2))/2

        plt.scatter([b], [0], s=80, color="royalblue", label="Source", zorder=3)
        plt.scatter([t1, t2], [0, 0], s=80, color="firebrick", label="Images", zorder=3)
    else:
        # Perfect alignment -> Einstein Ring
        phi = np.linspace(0, 2*np.pi, 200)
        ring_x = theta_e * np.cos(phi)
        ring_y = theta_e * np.sin(phi)

        plt.scatter([0], [0], s=80, color="royalblue", label="Source", zorder=3)
        plt.plot(ring_x, ring_y, color="firebrick", lw=3, label="Einstein Ring", zorder=3)

    plt.scatter(0, 0, s=120, color='black', marker='o', label='Lens', zorder=4)

    plt.xlim(-2.5, 2.5)
    plt.ylim(-2.5, 2.5)
    plt.gca().set_aspect('equal')

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper right')
    plt.title(f'Source Alignment: $\\beta = {b}$')
    plt.xlabel(r'$\theta_x / \theta_E$')
    plt.ylabel(r'$\theta_y / \theta_E$')

    plt.show()