import time
import random
def measure_dict_get_time(dict_size,num_trials=1000):
    test_dict={i:random.random() for i in range(dict_size)}
    access_time=[]

    for _ in range(num_trials):
        key=random.randint(0,dict_size-1)
        start_time=time.time()
        _=test_dict.get(key)
        end_time=time.time()

        access_time.append(end_time-start_time)
    return sum(access_time)/num_trials

def measure_dict_set_time(dict_size,num_trials=1000):
    test_dict={i:random.random() for i in range(dict_size)}
    set_time=[]

    for _ in range(num_trials):
        key=random.randint(0,dict_size-1)
        value=random.random()
        start_time=time.time()
        test_dict[key]=value
        end_time=time.time()

        set_time.append(end_time-start_time)
    return sum(set_time)/num_trials

dict_sizes=[10**3,10**4,10**5,10**6,10**7]

get_result={}
set_result={}

for size in dict_sizes:
    avg_get_time=measure_dict_get_time(size)
    avg_set_time=measure_dict_set_time(size)
    get_result[size]=avg_get_time
    set_result[size]=avg_set_time
    print(f"dict size:{size},Average get time:{avg_get_time:.10f} seconds,Average set time:{avg_set_time:.10f} seconds")
