import keyboard


class Pseudo:
    def __init__(self):
        self._value = 0

    def set_num(self, num):
        self._value = num

    def get_num(self):
        keyboard.wait([2, 3])
        return self._value

    def run_algorithm(self):
        for i in range(10):
            print(f"pressed on iter {i} by {self.get_num()}")


pseudo = Pseudo()
pseudo.run_algorithm()