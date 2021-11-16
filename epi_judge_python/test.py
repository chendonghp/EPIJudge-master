## module taylor
'''X,Y = taylor(deriv,x,y,xStop,h).
    4th-order Taylor series method for solving the initial
    value problem {y}’ = {F(x,{y})}, where
    {y} = {y[0],y[1],...y[n-1]}.
    x,y = initial conditions
    xStop = terminal value of x
    h = increment of x used in integration
    deriv = user-supplied function that returns the 4 x n array
    [y'[0] y'[1] y'[2] ... y'[n-1]
    y"[0] y"[1] y"[2] ... y"[n-1]
    y"'[0] y"’[1] y"’[2] ... y"’[n-1]
    y""[0] y""[1] y""[2] ... y""[n-1]]
'''
from numpy import array


def taylor(deriv, x, y, xStop, h):
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:  # Loop over integration steps
        h = min(h, xStop - x)
        D = deriv(x, y)  # Derivatives of y
        H = 1.0
        for j in range(4):  # Build Taylor series
            H = H * h / (j + 1)
            y = y + D[j] * H  # H = hˆj/j!
        x = x + h
        X.append(x)  # Append results to
        Y.append(y)  # lists X and Y
    return array(X), array(Y)  # Convert lists into arrays


## module printSoln
'''printSoln(X,Y,freq).
Prints X and Y returned from the differential
equation solvers using printput frequency ’freq’.
freq = n prints every nth step.
freq = 0 prints initial and final values only.
'''


def printSoln(X, Y, freq):
    def printHead(n):
        print("\tx\t", end='')
        for i in range(n):
            print("y[", i, "]\t\t", end='')
        print()

    def printLine(x, y, n):
        print("%13.4e " % x, end='')
        for i in range(n):
            print("%13.4e " % y[i], end='')
        print()

    m = len(Y)
    try:
        n = len(Y[0])
    except TypeError:
        n = 1
    if freq == 0: freq = m
    printHead(n)
    for i in range(0, m, freq):
        printLine(X[i], Y[i], n)
    if i != m - 1: printLine(X[m - 1], Y[m - 1], n)

from numpy import array, zeros
# from printSoln import *
# from taylor import *

def deriv(x,y):
    D = zeros((4,2))
    D[0] = [y[1] , -0.1*y[1] - x]
    D[1] = [D[0,1], 0.01*y[1] + 0.1*x - 1.0]
    D[2] = [D[1,1], -0.001*y[1] - 0.01*x + 0.1]
    D[3] = [D[2,1], 0.0001*y[1] + 0.001*x - 0.01]
    return D

x = 0 # Start of integration
xStop = 20 # End of integration
y = array([0.0, 1.0]) # Initial values of {y}
h = 5 # Step size
freq = 1 # Printout frequency
X,Y = taylor(deriv,x,y,xStop,h)
printSoln(X,Y,freq)
