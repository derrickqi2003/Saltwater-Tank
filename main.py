from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import rad2deg
import math
#gravitational
G = 6.67*10**-20 # km^3/(kg * s^2)
xval = [152.4055*10**6,152 * 10**6, 0]
px = []
py = []
txval = []
yval = [0, 0,0]
tyval = []
vx = [0,0,0]
tvx = []
vy = [30.32,29.295,0]
tvy = []
mass = [7.3476*10**22,5.972*10**24,1.989*10**30]
# every frame is 10,000 seconds
dt = 10000
numplanets = len(xval)

def calcDistance(i,index):
    dx = xval[i] - xval[index]
    dy = yval[i] - yval[index]
    mag = calcMag(dx,dy)
    return mag
def calcMag(x,y):
    mag =(x**2+y**2)**(1/2)
    return mag
def calcForce(i,index):
    m1 = mass[index]
    m2 = mass[i]
    #calculates the distance
    r = calcDistance(i,index)
    force = (G*m1*m2)/(r**2)
    return force
def calcDir(x,y):
    #this is for the arctan restrictions, separates it by quadrant
    if y > 0 and x <= 0:
        return (math.atan(y/x) +math.pi)
    if y <= 0 and x < 0:
        return (math.atan(y/x)+ math.pi)
    if x>0 and y <0:
        return math.atan(y/x)
    else:
        #returns an angle
        return math.atan(y/x)
def calcTotalEnergy():
    #Gives energy in km^2 s^-2
    #One km^2 s^-2 = 10^6 J
    E = 0
    for x in range(0,numplanets):
        E += mass[x]*calcMag(vx[x],vy[x])
        for i in range(0,numplanets):
            if i != x:
                E += -1*G*mass[i]*mass[x]/((calcDistance(i,x)))
    return E

def calcNetForce(index):
    xforce = 0
    yforce = 0
    for i in range(0,numplanets):
        if i != index:
            theta = calcDir(xval[i]-xval[index],yval[i]-yval[index])
            xforce += calcForce(i,index)*math.cos(theta)
            yforce += calcForce(i,index)*math.sin(theta)
    netdirection = calcDir(xforce,yforce)
    sumforce = calcMag(xforce,yforce)
    netforce = [sumforce,netdirection]
    return netforce
def moveobj(index):
    netforce = calcNetForce(index)
    a = netforce[0]/mass[index]
    ax= a*math.cos(netforce[1])
    ay = a*math.sin(netforce[1])
    dx = (1/2)*ax*(dt**2) + vx[index]*dt
    dy = (1 / 2) * ay * (dt**2) + vy[index]*dt
    global txval
    global tyval
    global tvx
    global tvy
    txval.append(dx+ xval[index])
    tyval.append(dy+ yval[index])
    tvx.append(ax * dt + vx[index])
    tvy.append(ay * dt + vy[index])
def update(i):
    for x in range(0,numplanets):
        moveobj(x)
    global xval
    global yval
    global vx
    global vy
    global txval
    global tyval
    global tvx
    global tvy
    xval = txval[:]
    yval = tyval[:]
    vx = tvx[:]
    vy = tvy[:]
    #clearing the temporary arrays. This part is unnecessary but i was too lazy to remove
    txval.clear()
    tyval.clear()
    tvx.clear()
    tvy.clear()
    plt.cla()
    #blue is path, red it planet
    plt.scatter(px, py, c="b")
    plt.scatter(xval,yval,c="r")
    for x in range(0, numplanets):
        px.append(xval[x])
        py.append(yval[x])
    plt.xlim(-2*10**8, 2*10**8)
    plt.ylim(-2*10**8, 2*10**8)
    print("Total Energy:")
    print(calcTotalEnergy())
    print("Kinetic Energy of the earth")
    print((1/2)* mass[1]*(calcMag(vx[1],vy[1])**2))
ani = FuncAnimation(plt.gcf(),update,interval=1)
plt.scatter(xval,yval)
plt.show()
