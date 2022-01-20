from threading import active_count, Thread
import time 

max_threads = 10
counter = 0

def my_function(my_argument_1, my_argument_n):
	"""do stuff"""
	return 

for __thing__ in __iterator__:
	counter +=1
		### for restarts - tricky to use... we don't know where the __thing__  *is* in realtime... 
		### so counter id can be +/- max_threads from any __thing__ thats failed..  
	if counter > 0:
			### maintains limit of max_threads threads being processed at any time (25 is limit of alma, around 15 seems to be sanest for disk writes) 
			while active_count() >= max_threads:
				time.sleep(.1)
			### starts a thread to do the work
			Thread(target=my_function, args=[my_argument_1,my_argument_n]).start()