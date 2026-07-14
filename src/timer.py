import time

def start_time():   

# This will start timer
    
   return time.perf_counter()

def end_time():
# This will pause timer

   return time.perf_counter()

def elapsed_time(start_time,end_time):
# This is the total time taken
   
   return int(end_time - start_time)/60  # Converting it to minutes to make it later useful


  