import time
import threading


def main():

    def func(name):
        print("Hello {name}.".format(name=name))
        time.sleep(4)
        print("Goodbye {name}.".format(name=name))


    thread1 = threading.Thread(target=func, args=["Mohamad"])
    thread2 = threading.Thread(target=func, args=["Mohamad"])
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
