import time
from random import randrange
def findmin(alist):
    overallMin=alist[0]
    for i in alist:
        issmallest=True
        for j in alist:
            if i>j:
                issmallest=False
        if issmallest:
            overallMin=i
    return overallMin

def findMin(alist):
    minsofar=alist[0]
    for i in alist:
        if i <minsofar:
            minsofar=i
    return minsofar
print(findmin([1,2,3,6,1,8]))

for listsize in range(1000,10001,1000):
    alist=[randrange(100000) for x in range(listsize)]
    start=time.time()
    print(findmin(alist))
    end=time.time()
    print("size:%d time %f" %(listsize,end-start))
        