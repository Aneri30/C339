# saving and reteriving custom object from npy file
import numpy as np
class Myclass:
    def __init__(self,value1,valye2):
        self.value=value1
        self.value2=valye2
    
obj= Myclass(42,'Aneri')
np.save('abc.npy',obj)
loaded_obj=np.load('abc.npy',allow_pickle=True)
#print('jinaskdnklasd', loaded_obj)
loaded_obj_type=loaded_obj.item()
print(loaded_obj_type.value2)

