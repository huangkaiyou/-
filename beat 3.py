import numpy as np
import matplotlib.pyplot as plt
data= np.loadtxt("C:/Users/user/Downloads/3033.csv", delimiter=',',skiprows=27,usecols=(0, 1), encoding='utf')
time= np.array([])
voltage= np.array([])
# voltage= np.loadtxt("C:/Users/user/Downloads/Figure30-31'.csv", delimiter=',')
for i in data:
    time= np.append(time, i[0])
    voltage= np.append(voltage, i[1])

import numpy as np 
import matplotlib.pyplot as plt 
from iminuit import Minuit
from iminuit.cost import LeastSquares

def f(t, f1, f2, phi, a,c):
    return 2*a*np.cos(np.pi*(f1+f2)*t)*np.cos(np.pi*(f1-f2)*t+phi)+c


yerror=0.03
least_squares = LeastSquares(time, voltage, yerror,f)


#m = Minuit(least_squares, mu=np.mean(data), sigma=np.std(data))
m = Minuit(least_squares, f1=33, f2=30, phi= 0 ,c=0.01,a= 3)
m.migrad()
m.hesse()

plt.figure(figsize= (15, 6))
plt.errorbar(time, voltage, yerror, fmt=".", label="data", alpha=0.5)
plt.plot(time, f(time, *m.values), label="fit")
fit_info = [
    f"$\\chi^2$ / $n_\\mathrm{{dof}}$ = {m.fval:.1f} / {len(time) - m.nfit}",
]
for p, v, e in zip(m.parameters, m.values, m.errors):
    fit_info.append(f"{p} = ${v:.3f} \\pm {e:.3f}$")
plt.legend(title="\n".join(fit_info))
plt.savefig('30-33.png')
plt.show()
