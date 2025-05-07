def knapsack(weights, biodiversity, limit):
    n = len(weights) # length of the weights (which should be 5, since theres 5 total weights)
    dp = [[0] * (limit + 1) for j in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(limit + 1):
            if weights[i - 1] > w: # if wt[i-1] > w
                dp[i][w] = dp[i - 1][w] 
            else: # "otherwise"
                dp[i][w] = max(dp[i - 1][w],dp[i - 1][w - weights[i - 1]] + biodiversity[i - 1]) # implementation of what i wrote in the paper.
    return dp[n][limit], dp

weights = [6, 4, 5, 3, 7]
biodiversity = [1600, 1000, 1800, 1200, 2000]
limit = 18

max_score, dp = knapsack(weights, biodiversity, limit)
print("Maximum Score:", max_score)
