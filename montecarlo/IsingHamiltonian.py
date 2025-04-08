import numpy as np
import math      
import copy as cp       
import networkx as nx
import matplotlib.pyplot as plt
from montecarlo import *


class IsingHamiltonian:
    def __init__(self, G):
        self.G = G
        self.mu = np.zeros(len(G.nodes()))
        self.N = len(G.nodes())
    
    def energy(self, config):
        """Compute energy of configureation, 'config'
            .. math::
                E = \\left<\\hat{H}\\right>
            
        Parameters
        ----------
        config : BitString
        Returns
        -------
        energy : float
            Energy of the input configuration
        """

        en=0
        s1=0
        s2=0
        w=0
        mag=0
        str_config = str(config)
        count = 0
        m=0
        k=0

        for (i,j) in self.G.edges():
            for e in self.G.edges:
                w=self.G.edges[e]['weight']
            
            if str_config[i]=="0":
                s1=-1
            else:
                s1=1

            if str_config[j]=="0":
                s2=-1
            else:
                s2=1
            
            s = s1 * s2

            en = en + (s * w)

        while k < self.N:
            if str_config[k]=="0":
                m=-1
            else:
                m=1
            mag = mag + (self.mu[k]*m)
            k = k + 1

        return float(en+mag)
        
    def set_mu(self, mus):
        """Set the net magnetization, 'mus'

        Parameters
        ----------
        mus : np.array
        Returns
        -------
        mu : np.array
            Energy bias of the magnetic field
        """

        i = 0
        while i<len(mus):
            self.mu[i]= mus[i]
            i = i + 1
        return self.mu


    

    def compute_average_values(self, T):
        """Compute the average energy, magnetization, heat capacity, and magnetic susceptability of a graph, including the mu term
            .. math::
            
            Paramerers
            ----------
            T : int
            Returns
            -------
            E : float
                Average energy of the graph
            M : float
                Average magnetization of the graph
            HC : float
                Average heat capacity of the graph
            MS : float
                Average magentic susceptibility of the graph
            """
         
        E = 0.0
        M = 0.0
        Z = 0.0
        HC = 0.0
        MS = 0.0

        #write your function here!
        k = 1
        beta = 1/(k*T)
        i = 0

        e = 0
        e_square = 0
        E_square = 0

        m = 0
        m_square = 0
        M_square = 0

        P = 0

        bs = BitString(self.N)

        while i < 2**self.N:
            bs.set_integer_config(i)
            Z = Z + math.exp(-beta*self.energy(bs))
            i = i + 1

        j = 0
        while j < 2**self.N:
            bs.set_integer_config(j)
            P = math.exp((-beta*self.energy(bs)))/Z

            e = self.energy(bs)
            e_square = e * e
            E = E + (e*P)
            E_square = E_square + (e_square*P)

            m = bs.on() - bs.off()
            m_square = m * m
            M = M + (m*P)
            M_square = M_square + (m_square*P)

            j = j + 1

        HC = (E_square-(E**2))/(T**2)
        MS = (M_square-(M*2))/T

        return E, M, HC, MS   