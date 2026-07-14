import time

def start_time():   
    
    return time.perf_counter()

def end_time():
     
   return time.perf_counter

def elapsed_time(start_time,end_time):
   
   elapsed_time=end_time - start_time

   return elapsed_time
