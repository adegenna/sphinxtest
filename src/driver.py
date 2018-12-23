import numpy as np
from module1 import *
from module2 import *

def main():
    """This is the main driver script"""
    a = 7.0
    b = 3.0
    A = funcA(a,b)
    B = funcB(a,b)
    C = funcC(a,b)
    D = funcD(a,b)
    print(A,B,C,D)

if __name__ == '__main__':
    main()
    
