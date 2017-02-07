from math import *
from decimal import *

#Keeping distances in Armstrong
#Will work only for 2 variables, x and y
#constants
e2 = 14.4

#functions

def g(x,y):
    a = Decimal(-14.4) * (1/x + 1/y)
    b = Decimal(1090) * (Decimal(exp(-x/Decimal(0.33))) + Decimal(exp(-y/Decimal(0.33))))
    #return x**2 + y**2 - 6*x
    #a = (x-1)**2 * Decimal(exp(-1 * y**2))
    #b = y * (y+2) * Decimal(exp(-2 * x**2))
    return a+b

def f(x,y,h):
    a = (g(x+h,y) - g(x,y)) / h
    b = (g(x,y+h) - g(x,y)) / h
    c = [a,b]
    return c

def steepDescent(x,y,a,delta):
    h = Decimal('1E-3')
    g0 = g(x,y)
    fi = f(x,y,h)
    dg = Decimal('0.0')
    for i in xrange(0,2):
        dg += fi[i] ** 2
    dg = Decimal(sqrt(dg))
    b = a/dg
    while(dg > delta):
        x -= b*fi[0]
        y -= b*fi[1]
        h /= 2
        fi = f(x,y,h)
        dg = Decimal('0.0')
        for i in xrange(0,2):
            dg += fi[i] ** 2
        dg = Decimal(sqrt(dg))
        print "dg = %f" % dg
        if dg == 0:
            break
        b = a/dg
        g1 = g(x,y)
        if g1 > g0:
            a = a/2
        else:
            g0 = g1
    c = [x,y]
    return c

def main():
    delta = Decimal('1E-12')
    a = Decimal('0.1')
    x = Decimal('0.5')
    y = Decimal('0.5')
    ans = steepDescent(x,y,a,delta)
    print "%f %f" % (ans[0], ans[1])

if __name__ == '__main__':
    main()
