from enum import Enum


class PhilosopherStatus(Enum):
    THINKING = "T"
    EATING = "E"
    WAITING = "W"

    __str__ = lambda self: self.value


class Philosopher:
    def __init__(self, meals):
        self.left_hand = ""
        self.right_hand = ""
        self.status: PhilosopherStatus = PhilosopherStatus.THINKING
        self.meals = meals

    def __str__(self):
        return f"{self.left_hand} {self.status} {self.right_hand}"
