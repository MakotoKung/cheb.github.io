import pandas as pd
import time

def brute_force_knapsack(filename, budget_million):
    df = pd.read_excel(filename)
    names = df['โครงการ'].tolist()
    costs = df['งบประมาณ (ล้านบาท)'].tolist()
    profits = df['ผลตอบแทน (%)'].tolist()
    n = len(costs)
    budget = budget_million

    best_profit = 0
    best_combo = []

    start_time = time.time()  # เริ่มจับเวลา

    for i in range(1, 2 ** n):
        selected = [bool(i & (1 << j)) for j in range(n)]
        total_cost = sum(costs[j] for j in range(n) if selected[j])
        total_profit = sum(profits[j] for j in range(n) if selected[j])
        if total_cost <= budget and total_profit > best_profit:
            best_profit = total_profit
            best_combo = selected

    end_time = time.time()  # จบจับเวลา
    elapsed_time = end_time - start_time

    selected_projects = [names[i] for i in range(n) if best_combo[i]]

    print("=== Brute Force Method ===")
    print("ผลตอบแทนสูงสุด:", best_profit, "%")
    print("โครงการที่เลือก:", selected_projects)
    print(f"ใช้เวลาในการคำนวณ: {elapsed_time:.6f}  วินาที")

# ตัวอย่างการเรียกใช้งาน
#brute_force_knapsack("data_used for example.xlsx", 10000000)
brute_force_knapsack("data_for test.xlsx", 5)
