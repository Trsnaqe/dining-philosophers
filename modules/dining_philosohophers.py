from modules.philosohoper import Philosopher, PhilosopherStatus
from threading import Lock
import random
import time
from helpers.output_helpers import print_table


class DiningPhilosophers:
    def __init__(self, number_of_philosopher, meal_size):
        self.chopsticks = [Lock() for _ in range(number_of_philosopher)]
        self.philosophers = [Philosopher(meal_size)
                             for _ in range(number_of_philosopher)]

    def philosopher(self, i):
        while self.philosophers[i].meals > 0:
            self.philosophers[i].status = PhilosopherStatus.THINKING
            j = (i + 1) % 5

            time.sleep(random.random())
            if not self.chopsticks[i].locked():
                self.chopsticks[i].acquire()
                self.philosophers[i].left_hand = "-"

                print_table(self.philosophers)
                time.sleep(random.random())

                if self.chopsticks[j].locked():
                    self.chopsticks[i].release()
                    self.philosophers[i].left_hand = ""
                   
                    print_table(self.philosophers)
                else:
                    self.chopsticks[j].acquire()
                    self.philosophers[i].right_hand = "-"
                    self.philosophers[i].status = PhilosopherStatus.EATING

                    print_table(self.philosophers)

                    self.philosophers[i].meals -= 1
                    time.sleep(random.random())

                    self.chopsticks[j].release()
                    self.philosophers[i].right_hand = ''
                    
                    self.chopsticks[i].release()
                    self.philosophers[i].left_hand = ''

                    self.philosophers[i].status = PhilosopherStatus.THINKING

                    print_table(self.philosophers)
