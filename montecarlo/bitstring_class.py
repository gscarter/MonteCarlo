import numpy as np
import math      
import copy as cp       


class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        out = ""
        for i in self.config:
            out += str(i)
        return out

    def __eq__(self, other): 
        return all(self.config == other.config)
    
    def __len__(self):
        return len(self.config)

    def __str__(self):
        output = ""
        for i in self.config:
            output = output + str(i)
        return output


    def on(self):
        """
        Return number of bits that are on
        """
        on = 0
        i = 0
        while i < len(self.config):
            if self.config[i] == 1:
                on = on+1
            i=i+1
        return on


    def off(self):
        """
        Return number of bits that are on
        """
        off = 0
        i=0
        while i < len(self.config):
            if self.config[i] == 0:
                off = off+1
            i = i+1
        return off

    def flip_site(self,i):
        """
        Flip the bit at site i
        """
        self.i = i
        if self.config[i]==0:
            self.config[i]=1
        else:
            self.config[i]=0

    
    def integer(self):
        """
        Return the decimal integer corresponding to BitString
        """
        integer = 0
        i = 0
        while i<len(self.config):
            if self.config[i] == 0:
                temp = 0 * (2**((len(self.config)-1)-i))
            else:
                temp = 1  * (2**((len(self.config)-1)-i))
            integer = integer + temp
            i = i+1
        return integer
        

 

    def set_config(self, s:list[int]):
        """
        Set the config from a list of integers
        """
        self.s = s
        i=0
        while i<len(self.config):
            self.config[i] = s[i]
            i = i+1
        return self.config
        

    def set_integer_config(self, dec:int):
        """
        convert a decimal integer to binary
    
        Parameters
        ----------
        dec    : int
            input integer
            
        Returns
        -------
        Bitconfig
        """
        self.dec = dec

        i = dec
        bitconfig = []

        while i//2 > 0:
            temp = i % 2
            bitconfig.insert(0,temp)
            i = i//2
        bitconfig.insert(0,i%2)
        Digits = len(self.config)
        difference = Digits - len(bitconfig)

        j=0
        while j<difference:
            bitconfig.insert(0,0)
            j = j + 1
        
        output = self.set_config(bitconfig)
        return output