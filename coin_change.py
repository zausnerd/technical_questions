'''
Question 3 -- changePossibilities(amount,amount): Your quirky boss collects rare, old coins. 
They found out you're a programmer and asked you to solve something they've been wondering for a long time. 

Write a function that, given an amount of money and an array of coin denominations, computes the number of ways to make the amount of money with coins of the available denominations. 
'''


def recur_change(amount, coins, store):
    if amount == 0:
        return 1
    if amount < 0 or coins == []:
        return 0
    combo = (amount, len(coins))
    if combo not in store:
        store[combo] = recur_change(amount - coins[-1], coins, store) + recur_change(amount, coins[:-1], store)
    return store[combo]


def changePossibilities(amount, coins):
    return recur_change(amount, coins, {})

print(changePossibilities(4, [1, 2, 3]))
