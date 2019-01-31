n, k = [int(x) for x in input().split()]
diff = sorted([[i, abs(i - k)] for i in [int(x) for x in input().split()]], key=lambda x:x[1])
print(" ".join(list(map(str, [diff[i][0] for i in range(1,4)]))))
