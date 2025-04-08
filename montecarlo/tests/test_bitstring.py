import sys

import pytest

from montecarlo import *


def test_1():
    my_bs = BitString(8)
    my_bs.flip_site(2)
    my_bs.flip_site(2)
    assert(my_bs.config == [0,0,0,0,0,0,0,0]).all()
    
    my_bs.flip_site(2)
    my_bs.flip_site(7)
    my_bs.flip_site(0)
    tmp1 = np.array([1,0,1,0,0,0,0,1])
    assert((my_bs.config == tmp1).all())
    assert(len(my_bs) == 8)


def test_2():
    my_bs = BitString(13)
    my_bs.set_config([0,1,1,0,0,1,0,0,1,0,1,0,0])

    assert(my_bs.on() == 5)
    assert(my_bs.off() == 8)
    assert(my_bs.integer() == 3220)



def test_3():
    my_bs = BitString(20)
    my_bs.set_integer_config(3221)
    
    tmp = np.array([0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1])
    assert((my_bs.config == tmp).all())
  
    for i in range(1000):
        my_bs.set_integer_config(i)
        assert(my_bs.integer() == i)


def test_4():
    my_bs1 = BitString(13)
    my_bs1.set_config([0,1,1,0,0,1,0,1,1,0,1,0,0])
    
    my_bs2 = BitString(13)
    my_bs2.set_integer_config(3252)
    
    assert(my_bs1 == my_bs2)
    my_bs2.flip_site(5)
    assert(my_bs1 != my_bs2)

if __name__== "__main__":
    test_1()
    test_2()
    test_3()
    test_4()