import numpy as np
import math 
import random     
import copy as cp       
import networkx as nx
import matplotlib.pyplot as plt
from montecarlo import *

class MonteCarlo:
    def __init__(self, ham):
        self.ham = ham
        self.N = len(ham)
        self.config = BitString(self.N)



    def run(self, T, n_samples, n_burn):

        i=0
        j=0
        w=0
        r=0

        list_of_e = []
        list_of_m = []
       
        prop_config = cp.deepcopy(self.config)
        current_config = cp.deepcopy(self.config)
      

        while i<n_samples:
            j=0
            while j<(self.N):
    
                prop_config.flip_site(j)

                #print(w)

                print("prop_config:", prop_config)
                print("current_config:", current_config)

                print("prop_config energy:", self.ham.energy(prop_config))
                print("current_config energy:", self.ham.energy(current_config))

                e1 = self.ham.energy(current_config)
                e2 = self.ham.energy(prop_config)

                e1 = self.ham.energy(current_config)
                e2 = self.ham.energy(prop_config)

                if e2<e1:
                    w=1
                else:
                    w=math.exp(-(e2-e1)/T)
                
                r = random.random()

                print("w:", w)
                print("r", r)

                if w>r:
                    current_config.set_config(str(prop_config))
                else:
                    prop_config.set_config(str(current_config))
                
                list_of_e.append(e1)
                list_of_m.append(self.ham.mag(current_config))

                print("current_config:", current_config)

                j = j + 1

            i=i+1
            #print(list_of_e)
        return list_of_e, list_of_m






