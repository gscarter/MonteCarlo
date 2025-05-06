import sys
import numpy as np
import pytest
import montecarlo
import networkx as nx
#import graphbuilder


def test_1():
    N=6
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(N)])
    for e in G.edges:
        G.edges[e]['weight'] = Jval

   
    #initialize BitString
    ham = montecarlo.IsingHamiltonian(G)
    ham.set_mu([.1 for i in range(N)])

    #set temperature
    T = 2

    #run exact average values for comparison
    Eref, Mref, HCref, MSref = ham.compute_average_values(T)

    #run montecarlo
    mc = montecarlo.MonteCarlo(ham)
    E,M = mc.run(T=T, n_samples=100000,n_burn=100)
    print(np.sum(E))

    Eavg = np.mean(E)
    Estd = np.std(E)
    Mavg = np.mean(M)
    Mstd = np.std(M)

    HC = (Estd**2)/(T**2)
    MS = (Mstd**2)/T

    print("     E:  %12.8f E(ref):  %12.8f error: %12.2e " %(Eavg, Eref, Eavg - Eref))
    print("     M:  %12.8f M(ref):  %12.8f error: %12.2e " %(Mavg, Mref, Mavg - Mref))
    print("     HC: %12.8f HC(ref): %12.8f error: %12.2e " %(HC, HCref, HC - HCref))
    print("     MS: %12.8f MS(ref): %12.8f error: %12.2e " %(MS, MSref, MS - MSref))

if __name__== "__main__":
    test_1()