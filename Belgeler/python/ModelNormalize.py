import numpy as np
def Normalizasyon(veriset):
    minx=np.min(veriset)
    maxp=np.max(veriset)
    model=0.1+((veriset-minx)/(maxp-minx))*0.8
    return model    
