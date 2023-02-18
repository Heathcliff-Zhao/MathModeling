# 二维散乱点插值 面积 微元法 积分
# from mpl_toolkits import mplot3d
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.interpolate import griddata
# from scipy.interpolate import interp1d
#
# x = np.array([7.0,10.5,13.0,17.5,34.0,40.5,44.5,48.0,56.0,
#               61.0,68.5,76.5,80.5,91.0,96.0,101.0,104.0,106.5,
#               111.5,118.0,123.5,136.5,142.0,146.0,150.0,157.0,158.0])
# y1 = np.array([44,45,47,50,50,38,30,30,34,
#                36,34,41,45,46,43,37,33,28,
#                32,65,55,54,52,50,66,66,68])
# y2=np.array([44,59,70,72,93,100,110,110,110,
#              117,118,116,118,118,121,124,121,121,
#              121,122,116,83,81,82,86,85,68])
# xn = np.linspace(x.min(), x.max(), 300)
# f1=interp1d(x,y1,'cubic')
# y11=f1(xn)
# plt.plot(xn,y11)
# f2=interp1d(x,y2,'cubic')
# y21=f2(xn)
# plt.plot(xn,y21)
# plt.show()
# area=sum((y21-y11)*((x.max()-x.min())/300)/18**2*1600)
# print(area)

# 三维散乱点插值
# from mpl_toolkits import mplot3d
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.interpolate import griddata
#
# x = np.array([129, 140, 103.5, 88, 185.5, 195, 105, 157.5, 107.5, 77, 81, 162, 162, 117.5])
# y = np.array([7.5, 141.5, 23, 147, 22.5, 137.5, 85.5, -6.5, -81, 3, 56.5, -66.5, 84, -33.5])
# z = -np.array([4, 8, 6, 8, 6, 8, 8, 9, 9, 8, 8, 9, 4, 9])
# xy = np.vstack([x, y]).T
# xn = np.linspace(x.min(), x.max(), 100)
# yn = np.linspace(y.min(), y.max(), 100)
# xng, yng = np.meshgrid(xn, yn)
# zn = griddata(xy, z, (xng, yng), method='nearest')
# plt.rc('font', size=16)
# plt.rc('text')
# ax = plt.subplot(121, projection='3d')
# ax.plot_surface(xng, yng, zn, cmap='viridis')
# ax.set_xlabel('$x$')
# ax.set_ylabel('$y$')
# ax.set_zlabel('$z$')
# plt.subplot(122)
# c = plt.contour(xn, yn, zn, 8)
# plt.clabel(c)
# plt.show()

 