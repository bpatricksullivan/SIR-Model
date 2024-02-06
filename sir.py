import matplotlib.pyplot as plt
import numpy as np
ndays = 400
dt = .05 #time step in days
beta = 1./2.#infection rate
gamma = 1./15. #recovery rate

nu = 3E-5 #the death rate
mu = nu #the birth rate

nt = int(ndays/dt)
S = np.zeros(nt) #suceptible
I = np.zeros(nt) #infected
R = np.zeros(nt) #Recovered
t = np.arange(nt)*dt
N =3E8

I[0] = 10 #initial infected number
S[0] = N -I[0] #population susceptible
R[0] = 0.

for i in range(nt-1):
    S[i+1] = S[i] + (mu*N - beta*S[i]*I[i]/N - nu*S[i])*dt
    I[i+1] = I[i] + (beta*S[i]*I[i]/N -gamma*I[i]-nu*I[i])*dt
    R[i+1] = R[i] + (gamma*I[i]-nu*R[i])*dt 
    
    
fig = plt.figure(1); fig.clf()
plt.plot(t,S,'r',lw=3, label='Susceptible')
plt.plot(t,I,'g',lw=3, label='Infected')
plt.plot(t,R,'b',lw=3, label= 'Recovered')
fig.legend(); plt.xlabel('Days'); plt.ylabel('# of individuals')

fig2 = plt.figure(2); fig2.clf()
plt.semilogy(t[10:],S[10:],'r',lw=3, label='Susceptible')
plt.semilogy(t[10:],I[10:],'g',lw=3, label='Infected')
plt.semilogy(t[10:],R[10:],'b',lw=3, label= 'Recovered')
fig2.legend(); plt.xlabel('Days'); plt.ylabel('# of individuals')
plt.ylim(1,4E8)


