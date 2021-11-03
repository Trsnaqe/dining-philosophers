import random
import time
from threading import Thread, Lock
import pandas as pd
import numpy as np
import os
from copy import copy

grid = ["", "", "1", "", "", "5", "", "", "", "2", "", "", "", "", "", "", "4", "", "3", ""]
total_meal_left = 10 * 5
personel_meal = 10


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_table(philos):
    global total_meal_left
    df = {
        '0': [" ", " ", " ", f"{philos[0]}", f"{philos[0].meals} ", " ", " "],
        '1': [" ", " ", " ", " ", " ", f"{philos[1]}", f"{philos[1].meals} "],
        '2': [" ", f"{philos[4]}", f"{philos[4].meals} ", " ", " ", " "," "],
        '3': [" ", " ", " ", " ", " ", f"{philos[2]} ", f"{philos[2].meals} "],
        '4': [" ", " ", " ", f"{philos[3]} ", f"{philos[3].meals} ", " "," "],
    }
    df = pd.DataFrame(df)
    used_chopsticks = 0
    eating_philos = 0
    for i in range(len(philos)):
        if philos[i].status == 'E':
            eating_philos += 1
        if philos[i].left_hand:
            used_chopsticks += 1
        if philos[i].right_hand:
            used_chopsticks += 1
    time.sleep(0.1)
    clear()
    print(df.to_string(index=False, header=False))
    print(f"Number of eating philosophers: {eating_philos} / 5")
    print(f"Number of locked chopsticks: {used_chopsticks} / 5")
    print(f"Meals left: {total_meal_left} / {50}")

class Philosopher:
    def __init__(self, meals):
        self.left_hand = ""
        self.right_hand = ""
        self.status = "T"
        self.meals = meals

    def __str__(self):
        return f"{self.left_hand} {self.status} {self.right_hand}"


class DiningPhilosophers:
    def __init__(self, number_of_philosopher, meal_size):
        self.chopsticks = [Lock() for _ in range(number_of_philosopher)]
        self.philosophers = [Philosopher(meal_size) for _ in range(number_of_philosopher)]

    def philosopher(self, i):
        while self.philosophers[i].meals > 0:
            self.philosophers[i].status = 'T'
            j = (i + 1) % 5
            '''print("Philosopher %d is thinking" % i)'''
            time.sleep(random.random())
            if not self.chopsticks[i].locked():
                self.chopsticks[i].acquire()
                self.philosophers[i].left_hand = "-"
                '''print("Philosopher %d has the chopstick %d" % (i, i))'''
                print_table(self.philosophers)
                time.sleep(random.random())
                if self.chopsticks[j].locked():
                    self.chopsticks[i].release()
                    self.philosophers[i].left_hand = ""
                    '''print("The chopstick %d is locked, so chopstick %d is released" % (j, i))'''
                    print_table(self.philosophers)
                else:
                    self.chopsticks[j].acquire()
                    self.philosophers[i].right_hand = "-"
                    '''print("Philosopher %d has the chopsticks %d and %d" % (i, i, j))'''
                    '''print("Philosopher %d is eating" % i)'''
                    self.philosophers[i].status = 'E'
                    print_table(self.philosophers)
                    self.philosophers[i].meals -= 1
                    time.sleep(random.random())
                    self.chopsticks[j].release()
                    self.philosophers[i].right_hand = ''
                    '''print("Philosopher %d released chopstick %d" % (i, j))'''
                    self.chopsticks[i].release()
                    self.philosophers[i].left_hand = ''
                    '''print("Philosopher %d released chopstick %d" % (i, i))'''
                    self.philosophers[i].status = 'T'
                    print_table(self.philosophers)


def main():
    global total_meal_left
    n = 5
    m = 10
    dining_philosophers = DiningPhilosophers(n, m)
    philosophers = [Thread(target=dining_philosophers.philosopher, args=(i,)) for i in range(n)]
    for philosopher in philosophers:
        philosopher.start()
    while total_meal_left > 0:
        total_meal_left = sum([dining_philosophers.philosophers[i].meals for i in range(n)])
        time.sleep(0.1)
    for philosopher in philosophers:
        philosopher.join()


if __name__ == "__main__":
    main()
