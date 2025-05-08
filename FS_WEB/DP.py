import pandas as pd
import time

def dp_knapsack(filename, budget_million):
    df = pd.read_excel(filename)
    names = df['โครงการ'].tolist()
    costs = df['งบประมาณ (ล้านบาท)'].tolist()
    profits = df['ผลตอบแทน (%)'].tolist()
    n = len(costs)
    W = int(budget_million)

    dp = [[0] * (W + 1) for _ in range(n + 1)]

    start_time = time.time()  # เริ่มจับเวลา

    for i in range(1, n + 1):
        for w in range(W + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][int(w - costs[i - 1])] + profits[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    w = W
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= int(costs[i - 1])

    end_time = time.time()  # จบจับเวลา
    elapsed_time = end_time - start_time

    selected.reverse()
    selected_projects = [names[i] for i in selected]

    print("=== Dynamic Programming Method ===")
    print("ผลตอบแทนสูงสุด:", dp[n][W], "%")
    print("โครงการที่เลือก:", selected_projects)
    print(f"ใช้เวลาในการคำนวณ: {elapsed_time:.6f} วินาที")

# ตัวอย่างการเรียกใช้งาน
#dp_knapsack("data_used for example.xlsx", 10000000)
dp_knapsack("data_for test.xlsx", 10000000)

