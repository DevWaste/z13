class Kassa:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def top_up(self, amount):
        self.balance += amount
        print(f"Касса пополнена на {amount}. Текущий баланс: {self.balance}")

    def count_1000(self):
        thousands = self.balance // 1000
        print(f"В кассе {thousands} полных тысяч")

    def take_away(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} взято из кассы. Оставшийся баланс: {self.balance}")
        else:
            raise ValueError("Денег нет, но вы держитесь")


kassa1 = Kassa(500)
kassa1.count_1000()
kassa1.top_up(1000)
kassa1.take_away(1000)