# 二维散点拟合
# import numpy as np
# from matplotlib.pyplot import *

# x = np.linspace(0, 1, 11)
# y = np.array([-0.447, 1.978, 3.28, 6.16, 7.08, 7.34,
#               7.66, 9.56, 9.48, 9.30, 11.2])
# scatter(x, y)
# p = np.polyfit(x, y, 2)  # 这里的数字代表拟合多项式的最高次数
# print(p)
# x1 = np.linspace(0, 1, 50)
# y1 = 0
# for i in range(0, len(p)):
#     y1 += p[i] * pow(x1, len(p) - i - 1)
# rc('font', size=16)
# rc('text')
# plot(x1, y1, 'r', label='$p(x)$', linewidth=2)
# xlabel('$x$')
# ylabel('$y$', rotation=0)
# legend()
# show()

# 三维散点拟合
# import numpy as np
# from scipy.optimize import curve_fit
# from mpl_toolkits import mplot3d
# import matplotlib.pyplot as plt
# x0 = np.array([129, 140, 103.5, 88, 185.5, 195, 105,
#                157.5, 107.5, 77, 81, 162, 162, 117.5])
# y0 = np.array([7.5, 141.5, 23, 147, 22.5, 137.5, 85.5,
#                -6.5, -81, 3, 56.5, -66.5, 84, -33.5])
# z0 = -np.array([4, 8, 6, 8, 6, 8, 8, 9, 9, 8, 8, 9, 4, 9])
# xy0=np.vstack((x0,y0))
# def Pfun(t,a,b,c,d,e,f):
#     return a*t[0]**2+b*t[1]**2+c*t[0]+d*t[1]+e*t[0]*t[1]+f
# popt,pcov=curve_fit(Pfun,xy0,z0)
# print(popt)
# xn=np.linspace(70,5,200)
# yn=np.linspace(-85,5,150)
# X,Y=np.meshgrid(xn,yn)
# Z = popt[0]*X**2+popt[1]*X**2+popt[2]*X+popt[3]*Y+popt[4]*X*Y+popt[5]
# ax1=plt.subplot(111,projection='3d')
# ax1.plot_surface(X,Y,Z,cmap='viridis')
# ax1.set_xlabel('x');ax1.set_ylabel('y');ax1.set_zlabel('z')
# plt.show()

