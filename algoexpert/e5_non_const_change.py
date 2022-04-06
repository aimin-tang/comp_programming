def nonConstructibleChange(coins):
    coins.sort()
    psum = 0

    for coin in coins:
        if coin > psum + 1:
            return psum + 1
        psum += coin

    return sum(coins) + 1

coins = [5, 7, 1, 1, 2, 3, 20]
print(nonConstructibleChange(coins))