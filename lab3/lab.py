import math, numpy, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

v = lambda w1, w2: lambda x, y: w1(x, y) + w2(x, y) + math.sqrt(w1(x, y)**2 + w2(x, y)**2)
n = lambda w1, w2: lambda x, y: w1(x, y) + w2(x, y) - math.sqrt(w1(x, y)**2 + w2(x, y)**2)

a = 8
b = 5
c = 3
d = 4

w11 = lambda x, y: -x + c + abs(x - c)
w12 = lambda x, y: +x + c + abs(x + c)
w1  = n(w11, w12)
w21 = lambda x, y: -y + d + abs(y - d)
w22 = lambda x, y: +y + d + abs(y + d)
w2  = n(w21, w22)
w31 = lambda x, y: -y + b * (a - abs(x)) / (a - c) + abs(y - b * (a - abs(x)) / (a - c))
w32 = lambda x, y: +y + b * (a - abs(x)) / (a - c) + abs(y + b * (a - abs(x)) / (a - c))
w3  = n(w31, w32)
#w3 = lambda x, y: b**2 * (a - x)**2 / (a - c)**2 - y**2
w41 = lambda x, y: -x + a + abs(x - a)
w42 = lambda x, y: +x + a + abs(x + a)
w43 = lambda x, y: -c + abs(x) + abs(abs(x) - c)
w44 = lambda x, y: +c + abs(x) + abs(abs(x) + c)
w4  = n( n(w41, w42), n(w43, w44) )
#w4 = lambda x, y: (a**2 - x**2) * (x**2 - c**2)

w  = v( n(w1, w2), n(w3, w4) )

def getFigure( left, right, dx ):
    X = numpy.arange( left, right, dx )
    Y = numpy.arange( left, right, dx )
    X, Y = numpy.meshgrid(X, Y)

    Z = [[ w(xi, yi) for xi, yi in zip(x, y) ] for x, y in zip(X, Y) ]

    return X, Y, Z

def draw( x, y, z ):
    fig = plt.figure()
    ax  = fig.gca(projection='3d')

    surf = ax.plot_wireframe(x, y, z, rstride=1, cstride=1)
    #surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
    #                   linewidth=0, antialiased=False)
    
    ax.set_zlim(0, 20.01)

if __name__ == '__main__':
    x, y, z = getFigure( -10, 10, 0.25 )
    draw( x, y, z )

    plt.show()