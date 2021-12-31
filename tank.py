from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from graphics import *
import random
import numpy
from numpy.random import default_rng
import math
#b is the concentration of the liquid going into the tank
#e is the flow rate of salt water into the tank
#f is the flow rate of mixed water out of the tank
#Q is the quantity of salt in the tank
#dt is the amount of time that passes between instant
#V is the volume of the tank
#t is the time
t = 0
V = 100
b = 0
e = 1
Q = 10
f = 1
dt = 1
concentration = Q/V
particles = []
xVal = []
yVal = []
logY = []
win = GraphWin('Saltwater Tank', 200, 200)
tank = Rectangle(Point(10, 10), Point(190, 190))
tank.draw(win)
#finddQ returns how many grams of salt exit/leave the tank in dt seconds.
def finddQ():
    dQ = -dt*Q/V
    return dQ
#finddV returns how many liters of water exit/leave the tank in dt seconds
def finddV():
    dV = e*dt-f*dt
    return dV
#findRandom generates a random number between 15 and 185
def findRandom():
    return random.randint(15, 185)
def update(i):
    global Q
    Q = Q + finddQ()
    global V
    V = V + finddV()
    global t
    t = t + dt
    global concentration
    concentration = Q/V
    logC = math.log(concentration)
    xVal.append(t)
    yVal.append(concentration)
    logY.append(logC)
    plt.subplot(211)
    plt.cla()
    plt.scatter(xVal,yVal)
    plt.ylabel("Concentration (g/L)")
    plt.title("Salt Concentration Graph")
    plt.subplot(212)
    plt.cla()
    plt.scatter(xVal,logY)
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Log(Concentration) (g/L)")
    white = Rectangle(Point(11,11),Point(189,189))
    white.setFill('White')
    white.draw(win)
    for u in range(int(Q)):
        x = findRandom()
        y = findRandom()
        particle = Circle(Point(x,y), 1)
        particle.draw(win)
ani = FuncAnimation(plt.gcf(),update,interval=100)
plt.subplot(211)
plt.scatter(xVal,yVal)
plt.show()
plt.subplot(212)
plt.scatter(xVal,logY)
plt.show()
