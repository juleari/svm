import math, numpy, matplotlib.pyplot as plt
from scipy.misc import derivative

l  = 1.0
mp = 1
N  = 87
dx = 1e-2

u = lambda x: math.e**x * math.sin(x)**2
f = lambda x: 0.5 * math.e**x * \
            ( 4 * math.sin(2 * x) + 3 * math.cos(2 * x) + 1 )

A = 0
B = math.e**l * math.sin(l)**2 / l

h  = l / N
t  = [i * h for i in range(N + mp)]
B1 = lambda i, x: 1 if t[ i - 1 ] <= x and x < t[ i ] else 0

bas = lambda i: lambda x: B1( i, x ) * ( x - l ) * x
phi = [ bas(i) for i in range(mp, N + mp) ]

i0l = lambda f, dx = dx: sum( f(x) * dx for x in numpy.arange(0, l, dx) )
d2 = lambda i: lambda x: derivative(phi[i], x, dx, 2)
L  = lambda i, j: lambda x: d2(i)(x) * phi[j](x)
fp = lambda p: lambda x: f(x) * p(x)

a = [ [ i0l( L(i, j) ) for j in range(N) ] for i in range(N) ]
b = [ i0l( fp(p) ) for p in phi ]
C = numpy.linalg.solve(a,b)

y = lambda x: A + B * x + sum(c * p(x) for c, p in zip( C, phi ))

def draw( f, style, label ):
    x = numpy.arange(0, l, dx)
    y = map( f, x )
    plt.plot(x, y, linestyle=style, label=label)

if __name__ == '__main__':
    diff = sum( (u(x) - y(x))**2 for x in numpy.arange(0,l,dx))

    print 'difference is: %s' % diff
    
    draw(u, 'solid', 'u')
    draw(y, 'dashed', 'y')

#    for i in range(N):
#        X = numpy.arange(0,l,dx)
#        Y = [phi[i](x) for x in X]
#        plt.plot(X, Y,label=i)

    plt.legend()
    plt.show()