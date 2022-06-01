print(df)

print("Means")
print(df.mean())
print("\nStandard Deviations")
print(df.std())

print(f"\nMax value of scalar: {df['scalar'].max()} at time {df['scalar'].idxmax()}")