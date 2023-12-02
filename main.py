from modules.dining_philosohophers import DiningPhilosophers
from threading import Thread
import time
import configs.table_config as table_config


def main():
    n = table_config.number_of_philosopher

    dining_philosophers = DiningPhilosophers(
        n, table_config.personel_meal)
    philosophers = [
        Thread(target=dining_philosophers.philosopher, args=(i,)) for i in range(n)]

    for philosopher in philosophers:
        philosopher.start()

    while table_config.total_meal_left > 0:
        table_config.total_meal_left = sum(
            [dining_philosophers.philosophers[i].meals for i in range(n)])
        time.sleep(0.1)

    for philosopher in philosophers:
        philosopher.join()


if __name__ == "__main__":
    main()
