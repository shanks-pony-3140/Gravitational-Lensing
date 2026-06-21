import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('lensed_points.csv')
 
theta1_x=df["theta1_x/theta_E"].values
theta1_y=df["theta1_y/theta_E"].values
theta2_x=df["theta2_x/theta_E"].values
theta2_y=df["theta2_y/theta_E"].values





r1 = np.sqrt(theta1_x**2 + theta1_y**2)
r2 = np.sqrt(theta2_x**2 + theta2_y**2)

# Lens equation: beta = theta - theta_e^2 / theta
# Here coordinates are normalized by theta_E, so theta_e = 1
# beta = theta * (1 - 1/theta^2)
x1 = theta1_x * (1 - 1/r1**2)
y1 = theta1_y * (1 - 1/r1**2)
   
x2 = theta2_x * (1 - 1/r2**2)
y2 = theta2_y * (1 - 1/r2**2)

plt.style.use('seaborn-v0_8-darkgrid')
plt.figure(figsize=(8, 8))

plt.scatter(x1, y1, s=10, color="royalblue", label="From Image 1", alpha=0.6)
plt.scatter(x2, y2, s=10, color="firebrick", label="From Image 2", alpha=0.6)
plt.scatter(0, 0, s=100, color='black', marker='o', label='Lens')

plt.gca().set_aspect('equal')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xlabel(r'$\beta_x / \theta_E$')
plt.ylabel(r'$\beta_y / \theta_E$')
plt.title('Source Reconstruction from Lensed Points')

plt.show()
    
    
    
    
    
    
    
    
    