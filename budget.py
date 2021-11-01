class Budget:
    spent_money = 0

    def __init__(self, deposit, withdrawal):
        self.deposit = deposit
        self.withdrawal = withdrawal
        Budget.add_spent_money(withdrawal)

    def deposit_money(self, amount):
        self.deposit += amount

    def withdraw_money(self, amount):
        self.withdrawal += amount
        Budget.add_spent_money(amount)

    def get_deposited_money(self):
        return self.deposit

    def get_withdrawal_money(self):
        return self.withdrawal

    @classmethod
    def get_whole_spent_amount(cls):
        return cls.spent_money

    @classmethod
    def add_spent_money(cls, amount):
        cls.spent_money += amount

    def transfer_deposited_money(self, amount, to):
        self.deposit -= amount
        to.deposit += amount


class Food(Budget):
    spent_money_on_food = 0

    def __init__(self, deposit, withdrawal):
        super().__init__(deposit, withdrawal)
        Food.spent_money_on_food += withdrawal

    @classmethod
    def get_money_spent_on_food(cls):
        return cls.spent_money_on_food

    @classmethod
    def add_money_spent_on_food(cls, amount):
        cls.spent_money_on_food += amount

    def withdraw_money(self, amount):
        self.withdrawal += amount
        Budget.add_spent_money(amount)
        Food.spent_money_on_food(amount)


class Clothing(Budget):
    spent_money_on_clothing = 0

    def __init__(self, deposit, withdrawal):
        super().__init__(deposit, withdrawal)
        Clothing.spent_money_on_clothing += withdrawal

    @classmethod
    def get_money_spent_on_clothing(cls):
        return cls.spent_money_on_clothing

    @classmethod
    def add_money_spent_on_clothing(cls, amount):
        cls.spent_money_on_clothing += amount

    def withdraw_money(self, amount):
        self.withdrawal += amount
        Budget.add_spent_money(amount)
        Clothing.add_money_spent_on_clothing(amount)


class Entertainment(Budget):
    spent_money_on_entertainment = 0

    def __init__(self, deposit, withdrawal):
        super().__init__(deposit, withdrawal)
        Entertainment.spent_money_on_entertainment += withdrawal

    @classmethod
    def get_money_spent_on_entertainment(cls):
        return cls.spent_money_on_entertainment

    @classmethod
    def add_money_spent_on_entertainment(cls, amount):
        cls.spent_money_on_entertainment += amount

    def withdraw_money(self, amount):
        self.withdrawal += amount
        Budget.add_spent_money(amount)
        Entertainment.add_money_spent_on_entertainment(amount)
