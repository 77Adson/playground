#Znalezdz local minima i maxima

def maxProfitWithKTransactions(prices, k):
    prices.append(0)
    profit = -prices[0]
    i = 0
    while i < len(prices)-1:
        if prices[i] > prices[i+1]:
            profit += prices[i]
            profit -= prices[i+1]
            i += 1
        i += 1
    return profit


prices = [5, 11, 3, 50, 60, 90]
k = 2
print(maxProfitWithKTransactions(prices, k))
