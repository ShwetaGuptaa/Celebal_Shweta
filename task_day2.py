## multi processing 
import multiprocessing

def multiply_two(num): 
    print(str(num)+" multiply by 2 is "+str(num*2)+"\n")

def multiply_three(num):
    print( str(num)+" multiply by 3 is "+str(num*3)) 

if __name__=="__main__":
    prcs_1=multiprocessing.Process(target=multiply_two,args=(2,))
    prcs_2=multiprocessing.Process(target=multiply_three,args=(2,))
    # process 1 start
    prcs_1.start()
    # process 2 start
    prcs_2.start()
    # waiting for process 1 to finish
    prcs_1.join()
    # waiting for process 2 to finish
    prcs_2.join()
    print("Both the processes are done")


    ## communicating between two processes in multiprocessing
def multiply_two_1(num_list,q):
    for num in num_list: 
        q.put(num * num) 

def print_queue(q): 

    print("Queue elements:") 
    while not q.empty(): 
        print(q.get()) 
    print("Queue is empty now")

if __name__ == "__main__": 
 
    num_list = [1,2,3,4] 
  
    # creating multiprocessing Queue 
    q = multiprocessing.Queue() 
  
 
    prcs_1 = multiprocessing.Process(target=multiply_two_1, args=(num_list, q)) 
    prcs_2 = multiprocessing.Process(target=print_queue, args=(q,)) 
  
    # running process p1  
    prcs_1.start() 
    prcs_1.join() 
  
    # running process p2
    prcs_2.start() 
    prcs_2.join() 


     ## multi threading

import threading 

if __name__ == "__main__": 
    # creating thread 
    th1 = threading.Thread(target=multiply_two, args=(2,)) 
    th2 = threading.Thread(target=multiply_three, args=(2,)) 
  
    # starting thread 1 
    th1.start() 
    # starting thread 2 
    th2.start() 
  
    # wait for thread 1
    th1.join() 
    # wait for thread 2 
    th2.join() 
  
    # both threads completely executed 
    print("Both threads executed successfully") 