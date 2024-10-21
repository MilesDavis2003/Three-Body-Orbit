import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
#Assign relevant constants
G = 6.67e-11
M_e = 5.97e24
M_m = 7.35e22
D = 3.84e8
w = 2.7e-6
#Define the origin to be the center of mass
r_2 = -(M_m / (M_e - M_m)) * D
r_1 = (M_e / (M_e - M_m)) * D
#This function integrates over time the changing distances of the earth and moon with respect to the center of mass and the satelite
def C(t):
  x_1 = r_1 * np.cos(w * t)
  y_1 = r_1 * np.sin(w * t)
  x_2 = r_2 * np.cos(w * t)
  y_2 = r_2 * np.sin(w * t)
  return [x_1, y_1, x_2, y_2]
#Define relevenat equations including the coriolis and centrfugal forces for rotating refrence frame
def func(info, t):
  x, x_dot, y, y_dot = info

  x_1, y_1, x_2, y_2 = C(t)

  r_e = np.sqrt((x - x_2)**2 + (y - y_2)**2)
  r_m = np.sqrt((x - x_1)**2 + (y - y_1)**2)

  x_ddot = -1*G * M_e * (x-x_2) / r_e**3 - G * M_m * (x-x_1) / r_m**3 + 2*y_dot*w + w**2*x
  y_ddot = -1*G * M_e * (y-y_2) / r_e**3 - G * M_m * (y-y_1) / r_m**3 - 2*x_dot*w + w**2*y
  return x_dot, x_ddot, y_dot, y_ddot
#Making a list to show where the moon and earth are relative to the rotating satelite
tingsx = [C(0)[0], C(0)[2]]
tingsy = [C(0)[1], C(0)[3]]
#Create a Linear space integrating over time
t = np.linspace(0, 24*60*60*20, 1000000)
#Initial conditions
i_c = [0.1*D, 0, 0, 2000]
#Solve first order ODE
sol = odeint(func, i_c, t)
#Obtain the relevant x and y equtions
x_t = sol[:, 0]
y_t = sol[:, 2]
#Plot the behaviors
plt.plot(x_t, y_t, color = 'red')
plt.scatter(tingsx, tingsy)
plt.title('Satelite (y vs x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

plt.plot(t, y_t, color = 'red')
plt.title('Satelite (y vs t)')
plt.xlabel('t')
plt.ylabel('y')
plt.grid(True)
plt.show()

plt.plot(t, x_t, color = 'red')
plt.title('Satelite (x v t)')
plt.xlabel('t')
plt.ylabel('x')
plt.grid(True)
plt.show()
