#28/03
#import threading
import logging
import time

def thread_function(name):
    logging.info("Thread %s:starting ",name)
    #these would basically sleep the program for 2 seconds
    time.sleep(200)
    logging.info("Thread %s fineshing",name)


if __name__ =="__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format,level=logging.INFO,datefmt="%H:%M:%S")
    logging.info("Main : before creating thread")
    thread_function(1,)
    logging.info("Main : before running thread")
    
    logging.info("Main : wait untill the thread to finsh")
    
    logging.info("Main : all done")

    #%%
    import threading
    import logging
    import time

    def thread_fucntion(name):
        logging.info("Thread %s: starting", name)
        # Sleeping the code for x seconds
        time.sleep(5)
        logging.info("Thread %s finishing", name)

    if __name__ == "__main__":
        format = "%(asctime)s : %(message)s"
        logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
        logging.info("Main: Before creating thread")
        # Thread means another thread to create things in parallel
        x = threading.Thread(target=thread_fucntion, args=(1,))
        y = threading.Thread(target=thread_fucntion, args=('second',))
        logging.info("Main: before running thread")
        # Running thread
        x.start()
        # The thread is running but we can do parallel stuff until thread finishes!
        logging.info("Main:wait until the thread to finish")
        logging.info("We can do wathever we want in parallel while thread is running")
        # Now we can see how the thread ends in the middle of the loop! -> parallel
        for i in range(7):
            print(f"Sleep outside thread {i+1}s")
            time.sleep(1)
        x.join() # Wait until the thread finishes before continuing to run the next line in the code
        
        logging.info("Main: all done")


    # %%
    import threading
    import time
    import logging

    logging.basicConfig(level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-9s) %(message)s',)

    def f1():
        logging.debug('Starting')
        time.sleep(1)
        logging.debug('Exiting')

    def f2():
        logging.debug('Starting')
        time.sleep(2)
        logging.debug('Exiting')

    def f3():
        logging.debug('Starting')
        time.sleep(3)
        logging.debug('Exiting')

    t1 = threading.Thread(target=f1) # use default name
    t2 = threading.Thread(name='f2', target=f2)
    t3 = threading.Thread(name='f3', target=f3)

    t1.start()
    t2.start()
    t3.start()

    # %%
    import threading
    import time
    import logging

    logging.basicConfig(level=logging.DEBUG,
                        format='(%(threadName)-9s) %(message)s',)

    def n():
        logging.debug('Starting')
        logging.debug('Exiting')

    def d():
        logging.debug('Starting')
        time.sleep(5)
        logging.debug('Exiting')

    if __name__ == '__main__':

        t = threading.Thread(name='non-daemon', target=n)
        d = threading.Thread(name='daemon', target=d)
        d.setDaemon(True)

        d.start()
        t.start()

        d.join(2.0)
        print('d.isAlive()', d.isAlive())
        t.join()

    # %%
    import threading
    import logging
    import time

    def thread_function(name):
        logging.info("Thread %s:starting ",name)
        #these would basically sleep the program for 2 seconds
        time.sleep(32)
        logging.info("Thread %s fineshing",name)


    if __name__ =="__main__":
        format = "%(asctime)s :Application Name X %(message)s"
        logging.basicConfig(format=format,level=logging.INFO,datefmt="%D:%M:%Y %H:%M:%S")
        logging.info("Main : before creating thread")
        x=threading.Thread(target =thread_function,args=(1,))
        logging.info("Main : before running thread")
        x.start()
        logging.info("Main : wait untill the thread to finsh")
        logging.info ("would do some parallel stuff untill thread is sleeping")
        x.join(timeout=12)   #  ensure you main program doesnt get ended before the function
        logging.info("Main : all done")

    #%% 
    import logging
    import threading
    import time
    def thread_function(name):
        logging.info("Thread %s:starting ",name)
        #these would basically sleep the program for 2 seconds
        time.sleep(20)
        logging.info("Thread %s fineshing",name)

    if __name__ =="__main__":
        format="%(asctime)s : %(message)s"
        logging.basicConfig(format=format,level=logging.INFO,datefmt="%H:%M:%S")
        thread =list()
        for index in range(3):
            logging.info("Main : create and start thread %d ",index)
            x=threading.Thread(target=thread_function,args=(index,))
            thread.append(x)
            x.start()
        
        for index,thread in enumerate(thread):
            logging.info("Main before joining %d ",index)

            thread.join()
            logging.info("Main thread % d done ",index)

    # %%
    import logging
    import threading
    import time
    def thread_function(name):
        logging.info("Thread %s:starting ",name)
        #these would basically sleep the program for 2 seconds
        time.sleep(20)
        logging.info("Thread %s finishing",name)

    if __name__ =="__main__":
        format="%(asctime)s : %(message)s"
        logging.basicConfig(format=format,level=logging.INFO,datefmt="%H:%M:%S")
        thread =list()
        for index in range(3):
            stop_threads = False
            logging.info(f"Main : create and start thread %d,{index}, {threading.active_count()} thread objects currently alive")
            x=threading.Thread(target=thread_function,args=(index,))
            thread.append(x)
            x.start()
        
        for thread1 in thread:
            stop_threads= True
            logging.info("Main before joining")

            #thread1.stop()
            logging.info(f"Main thread done, ({threading.active_count()} thread objects currently alive)")


    # %%
    import threading
    import time

    class Mythread(threading.Thread):

        def __init__(self):
            super().__init__()
            self.stop_thread=False

        def run(self):
            while not self.stop_thread:
                print("thread is running")
                time.sleep(1)

            print("thread stopped")

    #%%
    mythread= Mythread()
    mythread.start()
    time.sleep(5)
    mythread.stop_thread=True
    mythread.join()
    print("Thread is finished")
    print(threading.active_count())

    # %%

    import logging
    import threading
    import time
    import concurrent.futures

    def thread_function(name):
        logging.info("Thread %s:starting ",name)
        #these would basically sleep the program for 2 seconds
        time.sleep(20)
        logging.info("Thread %s finishing",name)

    if __name__ =="__main__":
        format="%(asctime)s : %(message)s"
        logging.basicConfig(format=format,level=logging.INFO,datefmt="%H:%M:%S")
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(thread_function,range(5))
        logging.info("Main thread end")
