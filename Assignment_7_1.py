#Design python application which creates two thread named as even and odd. 
#Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers


import threading

def even():
    for i in range(1,11):
        if i%2==0:
            print(i)
def odd():
    for i in range(1,10):
        if i%2!=0:
            print(i)

def main()

    thread1 = threading.Thread(target=even, args=())
    thread2 = threading.Thread(target=odd, args=())
# Will execute both in parallel
    thread1.start()
    thread2.start()
# Joins threads back to the parent process, which is this
# program
    thread1.join()
    thread2.join()
if __name__ == "__main__":
    main()