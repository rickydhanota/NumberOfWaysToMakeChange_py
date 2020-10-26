# Number of ways to make change
#Given an array of distinct positive integers representing coin denominations and a single non negative integer n representing a target amount of money. Write a function that returns the number of ways to make change for that target amount using the given coin denominations.
# Note that an unlimited amount of coins is at your disposal

# n = 6
# denom = [1, 5]

#Sample output
# 2 // 1x1 + 1x5 and 6x1

def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n + 1)] #This creates an array of all 0's for the length of the value n. We could prolly structure this a different way and get the same out put, for ex; ways=[] for i in range(0, n): ways.append(0)
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]

print(numberOfWaysToMakeChange(10, [1, 5, 10, 25]))
#O(nd) time | O(n) space
# d in the time complexity is the number of denominations

#Another example is n = 10 and denoms = [1, 5, 10, 25]