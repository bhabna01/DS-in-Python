import time
import random
def measure_access_time(list_size,num_trials=1000):
    test_list=list(range(list_size))
    access_time=[]

    for _ in range(num_trials):
        index=random.randint(0,list_size-1)
        start_time=time.time()
        _=test_list[index]
        end_time=time.time()

        access_time.append(end_time-start_time)
    return sum(access_time)/num_trials

list_sizes=[10**3,10**4,10**5,10**6,10**7]

result={}

for size in list_sizes:
    avg_time=measure_access_time(size)
    result[size]=avg_time
    print(f"List size:{size},Average acess time:{avg_time:.10f} seconds")
