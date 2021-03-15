from multiprocessing import Pool
from time import time

def f(x):
    from time import sleep
    sleep (1)
    return x*x

if __name__ == '__main__':
    t1s = time()
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3 ,5 ,6]))
    t1e = time()
    t2s = time()

    with Pool(1) as p:
        print(p.map(f, [1, 2, 3 ,5 ,6]))
    t2e = time()

    print("| job 5 procces did in %s|"%(t1s-t1e))
    print("| job 1 procces did in %s|"%(t2s-t2e))