class turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s
        print(f"Перемещение вверх. Новая позиция: ({self.x}, {self.y})")

    def go_down(self):
        self.y -= self.s
        print(f"Перемещение вниз. Новая позиция: ({self.x}, {self.y})")

    def go_left(self):
        self.x -= self.s
        print(f"Перемещение влево. Новая позиция: ({self.x}, {self.y})")

    def go_right(self):
        self.x += self.s
        print(f"Перемещение вправо. Новая позиция: ({self.x}, {self.y})")

    def evolve(self):
        self.s += 1
        print(f"Скорость увеличена до {self.s}")

    def degrade(self):
        if self.s > 1:
            self.s -= 1
            print(f"Скорость уменьшена до {self.s}")
        else:
            raise ValueError("Скорость не может быть уменьшена до 0 или меньше")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        moves = (dx + self.s - 1) // self.s + (dy + self.s - 1) // self.s
        return moves
