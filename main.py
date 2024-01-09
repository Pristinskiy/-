import cmath
import matplotlib.pyplot as plt


zn =complex(500 ,0)

fmin=1500000
fmax=2050000
N=1000


l1 =35 *10**(-6)
c1 =202*10**(-12)

l2 =1 *10**(-6)
c2 =502 *10**(-12)

l3 =35 *10**(-6)
c3 =202 *10**(-12)

l4 = 1 *10**(-6)
c4 =502 *10**(-12)

l5 =35 *10**(-6)
c5 =202 *10**(-12)

frez1 = 1 / (2 * 3.14 * (l1 * c1)**0.5)
frez2 = 1 / (2 * 3.14 * (l2 * c2)**0.5)
frez3 = 1 / (2 * 3.14 * (l3 * c3)**0.5)
frez4 = 1 / (2 * 3.14 * (l4 * c4)**0.5)
frez5 = 1 / (2 * 3.14 * (l5 * c5)**0.5)

print(frez1*10**(-6))
print(frez2*10**(-6))
print(frez3*10**(-6))
print(frez4*10**(-6))
print(frez5*10**(-6))



z1_5n: list[complex] = []
K=[]
zampnorm=[]

for f in range(fmin, fmax,N):


    xl1 = complex(0, (2 * 3.14 * f * l1))
    xl2 = complex(0, (2 * 3.14 * f * l2))
    xl3 = complex(0, (2 * 3.14 * f * l3))
    xl4 = complex(0, (2 * 3.14 * f * l4))
    xl5 = complex(0, (2 * 3.14 * f * l5))
    xc1 = complex(0, (-1 / (2 * 3.14 * f * c1)))
    xc2 = complex(0, (-1 / (2 * 3.14 * f * c2)))
    xc3 = complex(0, (-1 / (2 * 3.14 * f * c3)))
    xc4 = complex(0, (-1 / (2 * 3.14 * f * c4)))
    xc5 = complex(0, (-1 / (2 * 3.14 * f * c5)))
    z1: complex = (xl1 * xc1) / (xl1 + xc1)
    z2: complex = (xl2 + xc2)
    z3: complex = (xl3 * xc3) / (xl3 + xc3)
    z4: complex = (xl4 + xc4)
    z5: complex = (xl5 * xc5) / (xl5 + xc5)
    z5n=(zn * z5) / (zn + z5)
    z54=z5n+z4
    z53=z54*z3/(z54+z3)
    z52 = z53+z2
    z51=z52*z1/(z52+z1)
    K= (z51*z53*z5n) / (zn*z52*z54)


    z1_5n.append(K)
    amplitudes = [abs(z) for z in z1_5n]

for i in range(len(amplitudes)):
    zampnorm.append(amplitudes[i]/max(amplitudes))


    zamp = [round(x, 2) for x in zampnorm]
print(zamp)
# Ваш список значений (zamp))
# Создание списка индексов для значений (0, 1, 2, ...)
indices = range(fmin, fmax, N)
# Построение графика
plt.plot(indices, zamp, marker='o')  # Используем marker='o' для
# отображения точек на графике
plt.xlabel('Индексы')  # Подпись оси x
plt.ylabel('Значения')  # Подпись оси y
plt.title('График значений')  # Заголовок графика
plt.grid(True)  # Включение сетки
plt.show()  # Отображение графика



