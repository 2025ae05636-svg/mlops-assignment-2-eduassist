import pandas as pd
df = pd.read_csv("latency_tokens_cost.csv")
print(df.groupby("prompt_version").agg(
    mean_latency=("latency_seconds","mean"),
    median_latency=("latency_seconds","median"),
    min_latency=("latency_seconds","min"),
    max_latency=("latency_seconds","max"),
    avg_input_tokens=("input_tokens","mean"),
    avg_output_tokens=("output_tokens","mean"),
    avg_cost=("total_cost_usd","mean")
).round(6))
