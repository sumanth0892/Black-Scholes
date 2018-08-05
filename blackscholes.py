#Implied volatilities and value of European call option
from math import log,sqrt,exp
from scipy import stats
def call_value_initial(S0,K,T,r,sigma):
    S0 = float(S0) #Initial call option
    d1 = (log(S0/K)+(r+0.5*sigma**2)*T)/(sigma*sqrt(T))
    d2 = (log(S0/K)+(r-0.5*sigma**2)*T)/(sigma*sqrt(T))
    a = stats.norm.cdf(d1,0.0,1.0)
    b = stats.norm.cdf(d2,0.0,1.0)
    value = S0*a-K*exp(-r*T)*b
    return value

S0 = 100 
K=105
T=1
r=0.05
sigma = 0.2
call_value = call_value_initial(S0,K,T,r,sigma)
print ("The initial strike price is %5.3f" %call_value)




