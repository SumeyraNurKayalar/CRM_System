def assign_representatives(cost_matrix):
    n = len(cost_matrix)
    m = len(cost_matrix[0])
    assigned = set()
    assignments = []
    total_cost = 0

    for cust in range(m): # O(m)
        min_cost = float('inf')
        best_rep = -1

        for rep in range(n):  # O(n)
            if rep not in assigned and cost_matrix[rep][cust] < min_cost:
                min_cost = cost_matrix[rep][cust]
                best_rep = rep

        if best_rep != -1:
            assigned.add(best_rep)
            assignments.append((best_rep + 1, cust + 1))
            total_cost += min_cost

    return assignments, total_cost


cost_matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

assignments, total_cost = assign_representatives(cost_matrix)

print("\n\U0001F4CC Müşteri Temsilcisi Atamaları:")
for rep, cust in assignments:
    print(f"Temsilci {rep} -> Müşteri {cust}")
print(f"Toplam Atama Maliyeti: {total_cost}")

def knapsack(budget, costs, profits): # O(n * budget)
    n = len(costs)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(budget + 1):# O(budget)
            if costs[i - 1] <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - costs[i - 1]] + profits[i - 1])
            else:
                dp[i][b] = dp[i - 1][b]

    selected_campaigns = []
    b = budget
    for i in range(n, 0, -1): # O(n)
        if dp[i][b] != dp[i - 1][b]:
            selected_campaigns.append(i - 1)
            b -= costs[i - 1]

    return dp[n][budget], selected_campaigns


costs = [3, 4, 7, 8, 9]
profits = [4, 5, 10, 11, 13]
budget = 10

max_profit, selected_campaigns = knapsack(budget, costs, profits)

print("\n\U0001F4CC En İyi Pazarlama Kampanyaları:")
print(f"En Yüksek Yatırım Getirisi: {max_profit}")
print(f"Seçilen Kampanya Numaraları: {[i + 1 for i in selected_campaigns]}")
