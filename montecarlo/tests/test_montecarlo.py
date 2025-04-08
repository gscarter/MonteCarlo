"""
Unit and regression test for the montecarlo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

from montecarlo import *


def test_montecarlo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo" in sys.modules

def test_1():
    N = 6
    Jval = 2.0
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(N)])

    for e in G.edges:
        G.edges[e]['weight'] = Jval

    conf = BitString(N)
    ham = IsingHamiltonian(G)
    ham.set_mu(np.array([.1 for i in range(N)]))
    
    conf.flip_site(2)
    conf.flip_site(3)
    print(conf)
    e = ham.energy(conf)
    assert(np.isclose(e, 3.8))

def test_2():
    N = 6
    Jval = 2.0
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(N)])

    for e in G.edges:
        G.edges[e]['weight'] = Jval
    
    conf = BitString(N)
    ham = IsingHamiltonian(G)
    
    # Compute the average values for Temperature = 1
    E, M, HC, MS = ham.compute_average_values(1)
    
    print(" E  = %12.8f" %E)
    print(" M  = %12.8f" %M)
    print(" HC = %12.8f" %HC)
    print(" MS = %12.8f" %MS)
    
    assert(np.isclose(E,  -11.95991923))
    assert(np.isclose(M,   -0.00000000))
    assert(np.isclose(HC,   0.31925472))
    assert(np.isclose(MS,   0.01202961))

if __name__== "__main__":
    test_1()
    test_2()
