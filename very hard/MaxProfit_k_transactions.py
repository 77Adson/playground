def maxProfitWithKTransactions(prices, k):
    if not prices:
        return 0

    # Jeśli k >= n/2, można przeprowadzić dowolną liczbę transakcji
    n = len(prices)
    if k >= n // 2:
        return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))

    # Inicjalizacja tabeli DP(dynamiczne programowanie)
    dp = [[0] * n for _ in range(k + 1)]

    for t in range(1, k + 1):
        max_profit_before = -prices[0]
        for d in range(1, n):
            dp[t][d] = max(dp[t][d - 1], prices[d] + max_profit_before)
            max_profit_before = max(max_profit_before, dp[t - 1][d] - prices[d])

    return dp[k][n - 1]

