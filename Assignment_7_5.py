#Design python application which contains two threads named as thread1 and thread2. 
#Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on screen. 
#After execution of thread1 gets completed then schedule thread2.


import threading

def Values1():
    for i in range(51):
        print(i)
def Values2():
    for i in range(50,-1,-1):
        print(i)

def main():

    thread1 = threading.Thread(target = Values1, args=())
    thread2 = threading.Thread(target = Values2, args=())
# Will execute both in parallel
    thread1.start()
    thread1.join()
    thread2.start()

if __name__ == "__main__":  
    main()  