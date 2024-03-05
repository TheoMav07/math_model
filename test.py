import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.optimize import newton


def f(x):
    a = 1.2
    a = (((((((-4.46785*pow(10, 7) *(x-0.35)-989101) * (x-0.452028)-37580.9) * (x-0.0287786)+8202.96) * (x-0.2)+8588.79) * (x-0.40718)-2603.65) * (x-0.0897433)+1024.68) *(x-0.299966)-45.8766) *(x-0.5) *x
    if x > 0.5 or x < 0:
        return 0.0
    else:
        return a

def fd(v):
    c = 5.2
    c = (1.20473 * 0.00272415 * 0.5783 * np.square(v)) / 2
    return c

def avg(x):
    return sum(x) / len(x)

# x = np.linspace(0, 0.5, 500)
# y = f(x)

# plt.plot(x, y)
# plt.title("Thrust Force vs. Time")
# plt.xlabel("Time (s)")
# plt.ylabel("Thrust Force (N)")
# plt.show()

v = [0.0]
fDrag = [0.0]
fThrust = []
vStart = 0.0
vEnd = 0.0
J = 0.0
newJ = []
m = 0.07
vAvg = [0.0]

# J = integrate.quad(f, 0, 0.5)

for i in range(1, 3000):
    fThrust.append(f((0.0005*i)-0.0005))
    J = integrate.quad(f, (0.0005*i)-0.0005, 0.0005*i)
    vEnd = (J[0]/m) + vStart
    vStart = vEnd
    v.append(vEnd)
    fDrag.append(fd(vEnd))
fThrust.append(f(0.5))
vAvg.append(avg(v))
vEnd = 0.0
vStart = 0.0
v = []

# print(fThrust)

# y = np.array(fThrust)
# x = np.arange(float(len(y))) * 0.0005

# plt.plot(x, y)
# plt.show()

for i in range(0, 3*999):
    newJ.append((fThrust[i] - fDrag[i]) * 0.0005)
    vEnd = (newJ[i]/m) + vStart
    vStart = vEnd
    fDrag[i] = fd(vEnd)
    v.append(vEnd)
vAvg.append(avg(v))
vEnd = 0.0
vStart = 0.0

for k in range(1, 30):
    for i in range(0, 3*999):
        newJ[i] = (fThrust[i] - fDrag[i]) * 0.0005
        vEnd = (newJ[i]/m) + vStart
        vStart = vEnd
        v[i] = vEnd
        fDrag[i] = fd(vEnd)
    vAvg.append(avg(v))
    vEnd = 0.0
    vStart = 0.0


y = np.array(v)
x = np.arange(float(len(y))) * 0.0005

velocity_poly = np.polynomial.polynomial.Polynomial.fit(x, y, len(x))
# print(lagrange_poly)

# plt.scatter(x, y, label='Data')
# x_values = np.linspace(min(x), max(x), 100)
# plt.plot(x_values, lagrange_poly(x_values), color='red', label='Polynomial Fit')
# plt.legend()
# plt.show()

integral_value = 20
a = 0

def difference(b):
    integral, _ = integrate.quad(velocity_poly, a, b)
    return integral - integral_value

b = newton(difference, 1)
print("Final time: ", b)

integral = integrate.quad(velocity_poly, 0, b)
print(integral)

# plt.plot(x, y)
# plt.show()

# print(v[len(v) - 1])
