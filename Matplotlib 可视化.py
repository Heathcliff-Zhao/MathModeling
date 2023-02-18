# 二维平面上的已知散点
import numpy as np
from matplotlib.pyplot import *

x = np.array(range(8))
y = np.array([27.0, 26.8, 26.5, 26.3, 26.1, 25.7, 25.3, 24.8])
scatter(x, y)
show()

# 二维平面的曲线
# import numpy as np
# from matplotlib.pyplot import *
# x=np.linspace(0,2*np.pi,200)
# y1=np.sin(x)
# y2=np.cos(pow(x,2))
# rc('font',size=16)
# rc('text')
# plot(x,y1,'r',label='$sin(x)$',linewidth=2)
# plot(x,y2,'b--',label='$cos(x^2)$')
# xlabel('$x$')
# ylabel('$y$',rotation=0)
# legend()
# show()

# 三维空间的曲线
# from mpl_toolkits import mplot3d
# import matplotlib.pyplot as plt
# import numpy as np
# ax=plt.axes(projection='3d')
# z=np.linspace(0,100,1000)
# x=np.sin(z)*z
# y=np.cos(z)*z
# ax.plot3D(x,y,z,'k')
# plt.show()

# 三维空间的曲面
# from mpl_toolkits import mplot3d
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.linspace(-6,6,30)
# y=np.linspace(-6,6,30)
# X,Y=np.meshgrid(x,y)
# Z=np.sin(np.sqrt(X**2+Y**2))
# ax1=plt.subplot(1,2,1,projection='3d')
# ax1.plot_surface(X,Y,Z,cmap='viridis')
# ax1.set_xlabel('x');ax1.set_ylabel('y');ax1.set_zlabel('z')
# ax2=plt.subplot(1,2,2,projection='3d')
# ax2.plot_wireframe(X,Y,Z,color='c')
# ax2.set_xlabel('x');ax1.set_ylabel('y');ax1.set_zlabel('z')
# plt.show()

# 根据文本数据画等高线图及三位表面图
# from mpl_toolkits import mplot3d
# import matplotlib.pyplot as plt
# import numpy as np
#
# z = np.loadtxt("E:\Pdata2_42.txt")
# x = np.arange(0, 1500, 100)
# y = np.arange(1200, -10, -100)
# contr = plt.contour(x, y, z)
# plt.clabel(contr)  # 画等高线并标注
# plt.xlabel('$x$')
# plt.ylabel('$y$', rotation=0)
# plt.figure()
# ax = plt.axes(projection='3d')
# X, Y = np.meshgrid(x, y)
# ax.plot_surface(X, Y, z, cmap='viridis')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# plt.show()
