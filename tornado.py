

while True:
    if int(input())==0: break
    poste = [v=='1' for v in input().split(' ')]
    i = 0
    missing = []
    nbroke = 0
    for i in range(len(poste)):
        if not poste[i]:
            nbroke += 1
        else:
            missing.append(nbroke)
            nbroke = 0
    if len(missing) > 0:
        missing[0] += nbroke
        nrep = sum([m//2 for m in missing])
    else:
        nrep = (nbroke // 2) + (len(poste) % 2)
    print(nrep)
