import numpy as np
import matplotlib.pyplot as plt
from OuOb import pltSty2
# data=np.loadtxt("C:/Users/user/OneDrive/Desktop/b-1.txt")
ys= np.array([])
ys1= np.array([])
ys2= np.array([])
data=np.loadtxt("C:/Users/user/OneDrive/Desktop/week3_expdata/exp3_1.txt")
# data1=np.loadtxt("C:/Users/user/OneDrive/Desktop/week3_expdata/exp5_2.txt")
# data2=np.loadtxt("C:/Users/user/OneDrive/Desktop/week3_expdata/exp5_3.txt")
times= 13 #用幾組數據
dots= 5000 #取幾個數據點

R=5.1*10**3+50

err=0.01 #the allowed error
ignor=[]

#for discharge
'''
for k in range(10):
    y=data[k]
    index= 0
    x= np.linspace(0, 2,10000)
    for i in range(len(y)):
        if y[i]>3.1:
            index=i
            break
    for j in range(i, len(y)):
        if y[j]<2.9:
            index=j
            break
    plt.scatter(x[0:2000], y[index: index+2000],s=2,label= f'{k}')
'''
#for charge
for k in range(times):
    y=data[k]
    index= 0
    dt=2*10**-5
    x= np.array([0+i*dt for i in range(10000)])
    for i in range(len(y)):
        if y[i]<0.:
            index=i
            break
    for j in range(i, len(y)):
        if y[j]>0.3:
            index=j
            break
    ys=np.append(ys, y[j: j+dots])
data= np.reshape(ys, (int(len(ys)/times), times), order='F')
    
'''
    #skip the nonsense data
    i= 1 #initial data num
    now= j #present chosen data index 
    while i<dots+1:
        if abs(y[now]-y[now-1])>err :
            ignor.append(now)
        else :
            i+=1
    # plt.scatter(x[0:2000], y[index: index+2000],s=2,label= f'{k}'
    
    ys=np.append(ys, y[j: j+dots])
data= np.reshape(ys, (int(len(ys)/times), times), order='F')
'''


import numpy as np
import matplotlib.pyplot as plt
from iminuit import Minuit
from iminuit.cost import LeastSquares
xs=x[:dots]

ys= [np.mean(i) for i in data]

# yerror= [np.std(i) for i in data]
yerror=0.01/(2*3**(1/2))

ys1=[np.mean(i) for i in data1]
ys2=[np.mean(i) for i in data2]
def f(x, C, V, c): #charge 
    return V*(1-np.exp(-((x-c)/(R*C))))

least_square= LeastSquares(xs, ys, yerror= yerror, model= f)
m=Minuit(least_square, C=10**-6, V=3,c=-0.)
# plt.errorbar(xs, ys, yerr= stdev(ys)/ , fmt='')
m.migrad() 
m.hesse()
plt.errorbar(xs, ys, yerr=yerror, fmt="o", label="duty cycle=50",ms= 5, alpha= 0.8)
plt.errorbar(xs, ys1, yerr=yerror, fmt="o", label="duty cycle=40",ms= 2, alpha= 0.4)
plt.errorbar(xs, ys2, yerr=yerror, fmt="o", label="duty cycle=60",ms= 2, alpha= 0.4)
# plt.plot(xs, f(xs, *m.values), label="fit")

#for test
# plt.scatter(xs, ys, label= 'mean',s=2)
# plt.scatter(xs, y[j: j+dots], label= 'single', s=2)

fit_info = [
    f"$\\chi^2$ / $n_\\mathrm{{dof}}$ = {m.fval:.1f} / {len(xs) - m.nfit}",
]
for p, v, e in zip(m.parameters, m.values, m.errors):
    fit_info.append(f"{p} = ${v:.3e} \\pm {e:.3e}$")


ax1 = plt.subplot(1,1,1)
pltSty2(xName = 'Time t', yName = 'Voltage v')
# ax1.scatter(xs, ys, color = '#070d58', label = 'x(actual)', s = 5)
ax1.legend(loc = 'best', edgecolor = '#7e7474', fontsize = 12)

plt.tight_layout()
plt.draw()
# plt.xlabel('t (s)', fontsize= 15)
# plt.ylabel('V (volt)', fontsize= 15)
# plt.legend(title="\n".join(fit_info))
# plt.savefig('test.png',dpi= 500)
plt.show()
