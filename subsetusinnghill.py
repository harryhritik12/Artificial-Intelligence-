def subset_sum(set, target_sum):
    n = len(set)
    dp = [[None for j in range(target_sum+1)] for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = []

    for j in range(1, target_sum+1):
        dp[0][j] = []

    for i in range(1, n+1):
        for j in range(1, target_sum+1):
            if j < set[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                subset_without_i = dp[i-1][j]
                subset_with_i = [i-1] + dp[i-1][j-set[i-1]]
                if sum(set[index] for index in subset_with_i) == j:
                    dp[i][j] = subset_with_i
                else:
                    dp[i][j] = subset_without_i

    return dp[n][target_sum]




set = [3, 34, 4, 12, 5, 2]
target_sum = 9
print(subset_sum(set, target_sum))
