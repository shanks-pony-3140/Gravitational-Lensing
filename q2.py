import numpy as np 
import matplotlib.pyplot as plt

#the equatioon after substituting everythig becomes theta=beta + (theta_e)^2/tan(theta)
#we normalize theta_e=1 and solve for theta using newton-raphson

#at small theta the equation reduces to theta=beta+(theta_e)^2/theta,normalise theta_e to 1
#this reduces to aa quadratic equation where the solutions for theta are
#theta=(beta +(-) (beta^2+4)^(1/2))/2

def f(x,y):
    return x-y-1/np.tan(x)

def der(x):
    return 1+1/(np.sin(x)**2)

def approx(y):
    return (y+np.sqrt((y**2+4)))/2

def nr(x,y,f,der):
     return x - f(x,y)/der(x)

plt.style.use('seaborn-v0_8-darkgrid')

y_values = np.linspace(0.01, 2.5, 200)
margin = 1e-6
x_values = np.zeros(len(y_values))
x_approx = np.zeros(len(y_values))
error_values = np.zeros(len(y_values))

for i, y in enumerate(y_values):
    # use approximation as initial guess for NR
    x = approx(y)

    # Newton-Raphson to solve x - y - cot(x) = 0
    for _ in range(100):
        temp = nr(x, y, f, der)
        if abs(temp - x) < margin:
            x = temp
            break
        x = temp

    x_exact = x
    x_approximate = approx(y)
    
    # % error
    p = (abs(x_exact - x_approximate) / abs(x_exact)) * 100
    error_values[i] = p

plt.figure(figsize=(8, 5))
plt.plot(y_values, error_values, color='firebrick', lw=2)

plt.xlabel(r'$\beta/\theta_E$', fontsize=12)
plt.ylabel('Percentage Error (%)', fontsize=12)
plt.title('Error in Small-Angle Approximation', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
    