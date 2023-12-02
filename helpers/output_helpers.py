import time
import os
import pandas as pd
import configs.table_config as table_config
from modules.philosohoper import PhilosopherStatus


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_table(philos):
    df = {
        '0': [" ", " ", " ", f"{philos[0]}", f"{philos[0].meals} ", " ", " "],
        '1': [" ", " ", " ", " ", " ", f"{philos[1]}", f"{philos[1].meals} "],
        '2': [" ", f"{philos[4]}", f"{philos[4].meals} ", " ", " ", " ", " "],
        '3': [" ", " ", " ", " ", " ", f"{philos[2]} ", f"{philos[2].meals} "],
        '4': [" ", " ", " ", f"{philos[3]} ", f"{philos[3].meals} ", " ", " "],
    }
    df = pd.DataFrame(df)

    used_chopsticks = 0
    eating_philos = 0
    for i in range(len(philos)):
        if philos[i].status == PhilosopherStatus.EATING:
            eating_philos += 1
        if philos[i].left_hand or philos[i].right_hand:
            used_chopsticks += 1

    time.sleep(0.1)
    clear_screen()

    print(df.to_string(index=False, header=False))
    print(f"Number of eating philosophers: {eating_philos} / 5")
    print(f"Number of locked chopsticks: {used_chopsticks} / 5")
    print(f"Meals left: {table_config.total_meal_left} / {50}")
