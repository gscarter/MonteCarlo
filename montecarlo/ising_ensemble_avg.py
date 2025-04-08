def compute_average_values(bs:BitString, G: nx.Graph, T: float):

    E  = 0.0
    M  = 0.0
    Z  = 0.0
    HC = 0.0
    MS = 0.0

    # Write your function here!
    temp = T
    k = 1
    beta = 1/(k*temp)
    i = 0
    e = 0
    e_square = 0
    E_square = 0
    m = 0
    m_square = 0
    M_square = 0
    P = 0

    while i < 2**len(bs):
        bs.set_integer_config(i)
        #print(bs)
        Z = Z + math.exp(-beta*energy(bs, G))
        i = i + 1

    j = 0
    while j < 2**len(bs):
        bs.set_integer_config(j)
        P = math.exp((-beta*energy(bs,G)))/Z
    

        e = energy(bs,G)
        e_square = e*e
        E = E + (e*P)
        E_square = E_square + (e_square*P)

        m = bs.on() - bs.off()
        m_square = m*m
        M = M + (m*P)
        M_square = M_square + (m_square*P)

        j = j + 1

    HC = (E_square-(E**2))/(temp**2)
    MS = (M_square-(M*2))/temp
    
    return E, M, HC, MS