import numpy as np
import matplotlib.pyplot as plt
from iminuit import Minuit
from iminuit.cost import LeastSquares
from OuOb import pltSty2

# calculate the voltage of theory
def vr(f,r,l,c):
    xl = 2*np.pi*f*l
    xc =1/(2*np.pi*f*c)
    x = (xl - xc)
    z = np.sqrt(r**2 + x**2)
    return vin * abs(r/z)

def vc(f,r,l,c):
    xl = 2*np.pi*f*l
    xc =1/(2*np.pi*f*c)
    x = (xl - xc)
    z = np.sqrt(r**2 + x**2)
    return vin * abs(xc/z)

def vl(f,r,l,c):
    xl = 2*np.pi*f*l
    xc =1/(2*np.pi*f*c)
    x = (xl - xc)
    z = np.sqrt(r**2 + x**2)
    return vin * abs(xl/z)

def vs(f,r,l,c):
    return vin/f*f

def phase(f,r,l,c):
    xl = 2*np.pi*f*l
    xc =1/(2*np.pi*f*c)
    phase= np.arctan((xl-xc)/r)
    return phase

vin=3
print(1/(2*np.pi*(0.001*300e-12)**(1/2)))

#-----------------------------------------------

#fitting formula
def fitting(xs,a, f, phi, b):
    return a*np.sin(2*f*np.pi*xs+phi)

#initial condition
vin = 5
c =  290 * 10 ** -12
l = 1 * 10 ** -3
r= 993
n= 50 #change times
num= 1 #每幾個點取一個

yerror= 0.01 #each raw data errorbar (from oscilloscope)
initial= 1e5

# setting from labview
fre= np.array([int(initial+20000*i) for i in range(n)])

#fitting parameter
amp= []
ampr=[vr(f,r,l,c) for f in fre]
ampl=[vl(f,r,l,c) for f in fre]
ampc=[vc(f,r,l,c) for f in fre]
amps=[vs(f,r,l,c) for f in fre]

amp.append(ampr)
amp.append(ampl)
amp.append(ampc)
amp.append(amps)
#--------------------------------------------------------

#fitting result
phi= [] # Store phi data
phir=[]
phil=[]
phic=[]
phis=[]


phi.append(phir)
phi.append(phil)
phi.append(phic)
phi.append(phis)
#---------------------------------------------------------------------
phierr=[]
phirerr=[]
philerr=[]
phicerr=[]
phiserr=[]

phierr.append(phirerr)
phierr.append(philerr)
phierr.append(phicerr)
phierr.append(phiserr)
#-----------------------------------------------------------------------------

#input raw data
datar=[]
datac=[]
datal= []
datas=[]

#read data
datarr= np.loadtxt('C:/Users/user/OneDrive/Desktop/data-rlc/testr.txt')
datall= np.loadtxt('C:/Users/user/OneDrive/Desktop/data-rlc/testl.txt')
datass= np.loadtxt('C:/Users/user/OneDrive/Desktop/data-rlc/tests.txt')

datar= [[] for i in range(n)]
datal= [[] for i in range(n)]
datac= [[] for i in range(n)]
datas= [[] for i in range(n)]


for i in range(n):
    # print(len(datarr[i]))
    datar[i]= datarr[i][5000:]
    # print((datar))
    datal[i]= datall[i][5000:]
    datas[i]= datass[i][5000:]
    # print('ok')
angle= [[] for i in range(4)]
angle1= np.array([phase(f,r,l,c) for f in fre])
angle[0]= -angle1
angle[1]= -angle1+np.pi
angle[2]= -angle1-np.pi
angle[3]= np.array([0 for i in range(5000)])

'''
#transform into 2 order array
datarr= np.reshape(datarr, (n, 10000))
# datacc= np.reshape(datacc, (10000, n), order='F')
datall= np.reshape(datall, (n, 10000))
datass= np.reshape(datass, (n, 10000))
'''
datas= np.array(datas)
datal= np.array(datal)
datar= np.array(datar)
#get the individual voltage
datacc= (datas)-(datal)
datall= datal-(datar)
datass= datas
datarr= datar

'''
#select data
for j in range(n):
    for i in range(0, 10000, num): 
        datar.append(datarr[j][i])
        datac.append(datacc[j][i])
        datal.append(datall[j][i])
        datas.append(datass[j][i])

print('selection is successful')
'''
ys=[]
ys.append(datarr)
ys.append(datall)
ys.append(datacc)
ys.append(datass)

# i choose r, l, c, source
# j choose the data of specific frequency

# time=np.loadtxt("C:/Users/user/OneDrive/Desktop/test2r.txt") #sample period
dt= 2e-9
xs=np.array([0+dt*i for i in range(5000)])
ignor= []
color= ['red', 'tan', 'blue','seagreen' ]
label= ['R', 'L', 'C', 'Source']
print(amp[2][7])
for i in [0,1,2,3]:
    for j in range(n):
        
        # dt= time[j]

        least_square= LeastSquares(xs, ys[i][j], yerror, model= fitting)
        # print(amp[i][j], fre[j], angle[i][j], 0.)
        m=Minuit(least_square,a=amp[i][j], f= fre[j], phi=angle[i][j], b=0.)
        # # plt.errorbar(xs, ys, yerr= stdev(ys)/ , fmt='')
        m.migrad()
        m.hesse()
        
        fit_info = [
            f"$\\chi^2$ / $n_\\mathrm{{dof}}$ = {m.fval:.1f} / {len(xs) - m.nfit}",
        ]
        # ys= list(ys)
        # print((ys[i][j]))
        # plt.errorbar(xs, ys[i][j], yerr= yerror, fmt=".", color=color[i],ms= 2)
        # print((f(xs, *m.values)))
        # print(*m.values)
        # plt.plot(xs, fitting(xs, *m.values), label=label[i], color=color[i])
        # plt.plot(xs, f(xs, a=amp[i][j], f= fre[j], phi=0, b=0), label="theory")
        
        for p, v, e in zip(m.parameters, m.values, m.errors):
            fit_info.append(f"{p} = ${v:.3e} \\pm {e:.3e}$")
        # plt.legend(title="\n".join(fit_info))
        # plt.show()
        while abs(m.values['phi'])>1*np.pi:
            if abs(m.values['phi'])>3*np.pi:
                print(m.values['phi'])
                if j in ignor:
                    pass
                else:
                    ignor.append(j)
                break
 
            elif (m.values['phi'])>np.pi:
                (m.values['phi'])-=2*np.pi
            elif (m.values['phi'])< np.pi:
                (m.values['phi'])+=2*np.pi
        phi[i].append(m.values['phi'])
        phierr[i].append(m.errors['phi'])
        # print(i)
        # print(m.values['phi'])
    print('ok')

print((ignor))
fre= np.delete(fre, ignor)
for i in [0,1,2,3]:
    phi[i]= np.delete(phi[i], ignor)
    phierr[i]=np.delete(phierr[i], ignor)

plt.errorbar(fre, phi[1]-phi[0], phierr[1]-phierr[0], label= 'phase difference (L & R)')
plt.errorbar(fre, phi[2]-phi[0], phierr[2]-phierr[0], label= 'phase difference (C & R)')

ax1 = plt.subplot(1,1,1)
pltSty2(xName = 'Resistance r', yName = 'Time constant')
# ax1.scatter(xs, ys, color = '#070d58', label = 'x(actual)', s = 5)
plt.legend()
ax1.legend(loc = 'best', edgecolor = '#7e7474', fontsize = 12)

plt.grid()
plt.tight_layout()
plt.draw()
plt.xlabel('f (Hz)', fontsize= 10)
plt.ylabel('phi (rad)', fontsize= 10)
# plt.legend(title="\n".join(fit_info))
# plt.savefig('test.png',dpi= 500)
plt.show()
