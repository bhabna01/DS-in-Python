import time
import random

def measure_del_list_time(list_size,num_trials=1000):
    del_times=[]
    for _ in range(num_trials):
        test_list=list(range(list_size))
        index_To_Del=random.randint(0,list_size-1)
        start_Time=time.time()
        del test_list[index_To_Del]
        end_Time=time.time()
        del_times.append(end_Time-start_Time)
    return sum(del_times)/num_trials
def measure_del_dict_Time(dict_size,num_trials=1000):
    del_Times=[]
    for _ in range(num_trials):
        test_dict={i:random.random() for i in range(dict_size)}
        key_to_del=random.randint(0,dict_size-1)
        start_time=time.time()
        del test_dict[key_to_del]
        end_Time=time.time()
        del_Times.append(end_Time-start_time)
    return sum(del_Times)/num_trials

sizes=[10**3,10**4,10**5,10**6]
list_del_Results={}
dict_del_Results={}

for size in sizes:
    avg_list_del_time =measure_del_list_time(size)
    avg_del_dict_time=measure_del_dict_Time(size)
    list_del_Results[size]=avg_list_del_time
    dict_del_Results[size]=avg_del_dict_time
    print(f" Size:{size},list del time:{avg_list_del_time:.10f} seconds,Dict del time:{avg_del_dict_time:.10f} seconds")
