import numpy as np
import pandas as pd
np.random.seed(50)

def random_walk(n_steps):
    step= 0.5 - np.random.random(n_steps)
    return np.cumsum(step)

date =pd.date_range('1/1/2019','12/31/2019',freq='D')
data = {'a':random_walk(365), 'b':random_walk(365)}
df=pd.DataFrame(data,index=date)
df.head(365)