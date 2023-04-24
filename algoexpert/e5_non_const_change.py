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

# given a list of coins, find what amount can't be constructed.
# eg: [1, 2, 5], can't construct 4.
# sort first. increment psum from 0 with each coin.
# easy pitfall: need to return psum + 1.