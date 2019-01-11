a, b = input().split()
cost = abs(len(a)-len(b))
for i in range(min(len(a),len(b))):
  if a[i] != b[i]:
    cost += 1
print(cost)
