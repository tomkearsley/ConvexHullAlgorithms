import time
import convexhull


def giftwrap():
    '''Testing  (Gift-Wrapping Algorithm)'''
    setA = 'Set_A.dat'
    setB = 'Set_B.dat'
    print("---GIFT-WRAPPING TESTING---")
    print('Set A:')
    for i in range(2000,32000,2000):
        listPts = convexhull.readDataPts(setA,i)
        start = time.time()
        convexhull.giftwrap(listPts)
        end = time.time()
        elapsed = end-start
        print(elapsed)
    print()
    print('Set B:')
    for i in range(2000,32000,2000):
        listPts = convexhull.readDataPts(setB,i)
        start = time.time()
        convexhull.giftwrap(listPts)
        end = time.time()
        elapsed = end-start
        print(elapsed)    
        
def grahamscan():
    setA = 'Set_A.dat'
    setB = 'Set_B.dat'    
    '''Testing Graham Scan''' 
    print()
    print('------- GRAHAM SCAN -------')
    print('Set A:')
    for i in range(2000,32000,2000):
        listPts = convexhull.readDataPts(setA,i)
        start = time.time()
        convexhull.grahamscan(listPts)
        end = time.time()
        elapsed = end-start
        print(elapsed)
    print()
    print('Set B:')
    for i in range(2000,32000,2000):
        listPts = convexhull.readDataPts(setB,i)
        start = time.time()
        convexhull.grahamscan(listPts)
        end = time.time()
        elapsed = end-start
        print(elapsed)
        
def monotone_chaining():
    setA = 'Set_A.dat'
    setB = 'Set_B.dat'    
    '''Testing (Monotone Chain Testing)'''
    print()
    print("---MONOTONE CHAIN TESTING----")
    print('Set A:')
    for i in range(2000,32000,2000):
        listPts = convexhull.readDataPts(setA,i)
        start = time.time()
        convexhull.amethod(listPts)
        end = time.time()
        elapsed = end-start
        print(elapsed)
    print()
    print('Set B:')
    for i in range(2000,32000,2000):
        listPts = convexhull.readDataPts(setA,i)
        start = time.time()
        convexhull.amethod(listPts)
        end = time.time()
        elapsed = end-start
        print(elapsed) 
        
def main():
    giftwrap()
    #grahamscan()
    #monotone_chaining()

if __name__ == "__main__":
    main()
               