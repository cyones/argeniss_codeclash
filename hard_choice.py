


while True:
    try:
        av = [int(v) for v in input().split(' ')]
        re = [int(v) for v in input().split(' ')]
    except: break
    diff = sum([re[i] - av[i] for i in range(3) if re[i] > av[i]])
    print(diff)
