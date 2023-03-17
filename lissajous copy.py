import pylab
import matplotlib.pyplot as pylab
import math
import numpy as np

ratio_list= [30/30.1, 30/31]

phase_diff_list= [0, np.pi/4, np.pi/2]
#for experiment
period= 2*math.pi*math.sqrt(0.30/9.8)

def f(t):
    return 3*math.sin(30*t)
def g(t):
    return 3*math.sin(30*ratio*t+phase_diff)
ratio= 31/30
phase_diff= 0
# set up data interval
dx= 0.01
# set up the start\end point
a=0
b=50
# set up how many data
n= int((b-a)/dx )
# 產生座標點
ts= [ (a+dx*i) for i in range(n+1)]
xs= [ f(t) for t in ts]
ys= [ g(t) for t in ts]

# #subplots
# import matplotlib.pyplot as plt
# fig, ax =plt.subplots(1, 2)
# for i in range(2):
#     ratio= ratio_list[i]
#     for j in range(3):
#         phase_diff= phase_diff_list[j]
#         xs= [ f(t) for t in ts]
#         ys= [ g(t) for t in ts]
#         ax[i, j].plot(xs, ys)
        
        
print(1)
#animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax= plt.subplots()
ax.set_xlabel('x (cm)')
ax.set_ylabel(' y (cm)')

i= range(n+1)

#for animation
def run(i):
    ax.scatter(xs[i], ys[i]) #experiment
print(2)
# plt the animation   
ani= animation.FuncAnimation(fig, func=run, frames=i, interval=35)
plt.show()


#save the file
ims=[] #the photo storage
fig= plt.figure()
for i in range(n+1):
    if i >=50:
        im= plt.scatter(xs[i-50: i], ys[i-50: i]).findobj()
    else:
        im= plt.scatter(xs[:i], ys[:i]).findobj()
    ims.append(im)
ani= animation.ArtistAnimation(fig, ims,interval= 30) #interval determine the speed of animation
ani.save('lissa2.gif', writer= 'pillow')

print('finish') 
