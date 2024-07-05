#Work_in_progres

def maxProfitWithKTransactions(prices, k):
    prices.append(0)
    if prices[0] == max(prices):
        return 0
    profit = [-prices[0]]
    i = 0
    n = 0
    while i < len(prices) - 1:
        if prices[i] > prices[i + 1]:
            profit[n] += prices[i]
            profit[n] -= prices[i + 1]
            i += 1
            profit.append(0)
            n += 1
        i += 1
    print(profit)
    return bestK(profit, k)


def bestK(profit, k):
    profit.sort(reverse=True)
    profit = profit[:k]
    suma = sum(profit)
    return suma
