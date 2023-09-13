import statistics

x = [0.0, 0.0, 0.0, 0.0, 0.0]
y = [0.0, 0.0, 0.0, 0.0, 0.0]

for i in range(5):
    x[i] = float(input())

for j in range(5):
    y[j] = float(input())

x_med = statistics.mean(x)
x_medn = statistics.median(x)
x_dp = statistics.stdev(x)

y_med = statistics.mean(y)
y_medn = statistics.median(y)
y_dp = statistics.stdev(y)

xy_corre = statistics.correlation(x,y)

print(f"{x_med:.2f}")
print(f"{x_medn:.2f}")
print(f"{x_dp:.2f}")

print(f"{y_med:.2f}")
print(f"{y_medn:.2f}")
print(f"{y_dp:.2f}")

print(f"{xy_corre:.2f}")