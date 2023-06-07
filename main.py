import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork, waiter):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.waiter = waiter

    def run(self):
        while True:
            # request forks
            self.waiter.acquire()
            self.left_fork.acquire()
            self.right_fork.acquire()
            self.waiter.release()

            # eat
            print(f"{self.name} is eating...")
            time.sleep(random.uniform(1, 5)) # random eating time

            # release forks
            self.left_fork.release()
            self.right_fork.release()

            # think
            print(f"{self.name} is thinking...")
            time.sleep(random.uniform(1, 5)) # random thinking time


def main():
    num_philosophers = 5
    forks = [threading.Lock() for _ in range(num_philosophers)]
    waiter = threading.Lock()

    philosophers = []
    for i in range(num_philosophers):
        philosopher = Philosopher(f"Philosopher {i}", forks[i], forks[(i+1)%num_philosophers], waiter)
        philosophers.append(philosopher)

    for philosopher in philosophers:
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()


if __name__ == "__main__":
    main()
