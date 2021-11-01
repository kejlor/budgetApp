from budget import *

whole_budget = Budget(3000, 0)
entertainment = Entertainment(1000, 500)
food = Food(1000, 700)
clothing = Clothing(1000, 600)
print(entertainment.get_money_spent_on_entertainment())
print(food.get_money_spent_on_food())
print(clothing.get_money_spent_on_clothing())
print(whole_budget.get_whole_spent_amount())
