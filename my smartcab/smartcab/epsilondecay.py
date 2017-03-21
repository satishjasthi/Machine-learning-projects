import matplotlib.pyplot as plt
import math


def floatRange(x0, x1, points):
    step = 1.0*(x1 - x0)/(points-1)
    return [x0+step*x for x in range(0, points)]

def epsilondecay(t):
    return 1 - math.exp(-math.exp(-(1.0*t-4.0*30.0)/30.0))


if __name__ == '__main__':
    x = floatRange(0, 400, 300)
    y = list(map(epsilondecay, x))
    plt.plot(x, y)
    plt.show()
    print "new tolerance: {}".format(epsilondecay(400))

