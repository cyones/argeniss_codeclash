

while True:
    try: exp = [int(v) for v in input().split(' ')]
    except: break
    min_diff = float('inf')
    tot = sum(exp)
    for i in range(0, 10):
        for j in range(i+1, 10):
            for k in range(j+1, 10):
                for l in range(k+1, 10):
                    for m in range(l+1, 10):
                        expA = exp[i] + exp[j] + exp[k] + exp[l] + exp[m]
                        expB = tot - expA
                        diff = abs(expA - expB)
                        min_diff = min(diff, min_diff)
    print(min_diff)
