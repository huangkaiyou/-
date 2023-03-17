import matplotlib.animation as animation
import matplotlib.pyplot as plt

# canvas
fig, ax= plt.subplots()
ax.set_xlim(-9.2,-5)
ax.set_ylim(-5,-3)
ax.set_xlabel('x (cm)')
ax.set_ylabel(' y (cm)')

xs= []
ys= []
number= range(500) #how many data are going drawn
def run(i):
    ax.scatter(xs[i], ys[i]) #experiment


# plt the animation   
ani= animation.FuncAnimation(fig, func=run, frames=i, interval=350)
# plt.show()


#save the file
ims=[] #the photo storage
fig= plt.figure()
for i in range(number):
    if i >=10:
        im= plt.scatter(xs[i-10: i], ys[i-10: i]).findobj()
    else:
        im= plt.scatter(xs[i], ys[i]).findobj()
        ims.append(im)
ani= animation.ArtistAnimation(fig, ims,interval= 300) #interval determine the speed of animation
ani.save('pendulum1.gif', writer= 'pillow')

print('finish') 
