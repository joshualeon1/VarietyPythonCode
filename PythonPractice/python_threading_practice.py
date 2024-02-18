import threading
import math

def do_work(worker_id):
    print("Worker %s is starting..." % worker_id)
    #work below
    answer = (-6+math.sqrt(pow(6,2)-4*3*2))/(2*3)
    print("Answer: "+ str(answer))#Should be -0.42264
    print("Worker %s is done." % worker_id)

# Create a list of worker threads
threads = []
for i in range(5):
    t = threading.Thread(target=do_work, args=(i,))#target is callable object, args is a tuple
    threads.append(t)

# Start the threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("All workers are done.")