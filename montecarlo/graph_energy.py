def energy(bs: BitString, G: nx.Graph):
    """Compute energy of configuration, `bs`

        .. math::
            E = \\left<\\hat{H}\\right>

    Parameters
    ----------
    bs   : Bitstring
        input configuration
    G    : Graph
        input graph defining the Hamiltonian
    Returns
    -------
    energy  : float
        Energy of the input configuration
    """

    en=0
    s1=0
    s2=0
    w=0
    str_bs = str(bs)
    l=len(str_bs)

    for (i,j) in G.edges():

        for e in G.edges:
            w=G.edges[e]['weight']
       
        if str_bs[l-1-i]=="0":
            s1=1
        else:
            s1=-1
        
        if str_bs[l-1-j]=="0":
            s2=1
        else:
            s2=-1
        
        s = s1 * s2
        en = en + (s*w)
        
    
    return float(en)