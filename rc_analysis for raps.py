import numpy as np
import matplotlib.pyplot as plt
from OuOb import pltSty2
# data=np.loadtxt("C:/Users/user/OneDrive/Desktop/b-1.txt")
ys= np.array([])
ys1= np.array([])
ys2= np.array([])
data=np.loadtxt("C:/Users/user/OneDrive/Desktop/week3_expdata/exp3_1.txt")

# data2=np.loadtxt("C:/Users/user/OneDrive/Desktop/week3_expdata/v5.1k2.dat")
# data2*=5

times= 13 #用幾組數據
dots= 1500 #取幾個數據點

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
    for k in range(i, len(y)):
        if y[k]>0.3:
            index=k
            break
    ys=np.append(ys, y[k: k+dots])
data= np.reshape(ys, (int(len(ys)/times), times), order='F')

xs=x[:dots]
# plt.scatter(xs, y[k: k+dots], label= 'single', s=7,color='violet', alpha=1)

      
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


def f(x, tau, V, c): #charge 
    return V*(1-np.exp(-((x-c)/(tau))))
def g(x, tau, V, c): #charge 
    tau= 0.0051
    return V*(1-np.exp(-((x-c)/(tau))))

least_square= LeastSquares(xs, ys, yerror= yerror, model= f)
m=Minuit(least_square, tau=0.0051, V=3,c=-0.)
# plt.errorbar(xs, ys, yerr= stdev(ys)/ , fmt='')
m.migrad() 
m.hesse()
plt.errorbar(xs, ys, yerr=yerror, fmt="o", label="data",ms= 3, alpha=0.6, color='brown')

# plt.errorbar(xs1, ys2, yerr=yerror, fmt="o", label="raspberry pi",ms= 2)
# plt.plot(xs, f(xs, *m.values), label="fit", color= 'green')
plt.plot(xs, g(xs, *m.values), label="theory", color= 'blue', linestyle= 'dashed')
#for test
# plt.scatter(xs, ys, label= 'mean',s=2)


fit_info = [
    f"$\\chi^2$ / $n_\\mathrm{{dof}}$ = {m.fval:.1f} / {len(xs) - m.nfit}",
]
for p, v, e in zip(m.parameters, m.values, m.errors):
    fit_info.append(f"{p} = ${v:.3e} \\pm {e:.3e}$")

print(m.values['V'])
ax1 = plt.subplot(1,1,1)
pltSty2(xName = 'Time t', yName = 'Voltage v')
# ax1.scatter(xs, ys, color = '#070d58', label = 'x(actual)', s = 5)
ax1.legend(loc = 'best', edgecolor = '#7e7474', fontsize = 12)

plt.tight_layout()
plt.draw()
plt.grid(color= 'gray', visible=True)
# plt.xlabel('t (s)', fontsize= 15)
# plt.ylabel('V (volt)', fontsize= 15)
plt.legend(title="\n".join(fit_info))
# plt.savefig('test.png',dpi= 500)
plt.show()
