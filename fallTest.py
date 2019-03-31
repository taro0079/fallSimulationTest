####
# Import
####

import numpy as np
from matplotlib import pyplot as plt

#### 
# Constant
####

k = 1.2 # ばね定数
m = 100 # kg
mu = 0.9 # 摩擦係数
omega0 = np.sqrt(k/m)
kappa = mu/m


####
# differential equation 1 
# dx/dt = v
####

def f1(t):
    return v


####
# differential equation 2
# dv/dt = -kappa*v - omega**2*x
####
def f2(t):
    return - kappa*v - omega0**2 * x


#####
# ルンゲクッタ
#####

