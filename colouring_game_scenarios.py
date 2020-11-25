from collections import defaultdict


def ncc(img, n, m):
    lbl = [[None] * len(img[i]) for i in range(n)]
    cc = 0
    eqv = defaultdict(lambda: set())
    for i in range(n):
        for j in range(m):
            if not img[i][j]: continue
            if (
                j>0 and lbl[i][j-1] is not None and
                i>0 and lbl[i-1][j] is not None and
                lbl[i-1][j] != lbl[i][j-1]
            ):
                l1 = lbl[i][j-1]
                l2 = lbl[i-1][j]
                lbl[i][j] = l1
                eqv[l2].add(l1)
                eqv[l1].add(l2)
            elif j>0 and lbl[i][j-1] is not None:
                lbl[i][j] = lbl[i][j-1]
            elif i>0 and lbl[i-1][j] is not None:
                lbl[i][j] = lbl[i-1][j]
            else:
                eqv[cc].add(cc)
                lbl[i][j] = cc
                cc += 1

    cc = [i for i in range(len(eqv.keys()))]
    for i in eqv.keys():
        if len(eqv[i]) == 1: continue
        queue = [neig for neig in eqv[i] if cc[neig] != i]
        while len(queue) > 0:
            j = queue.pop()
            if cc[j]!=i:
                cc[j] = i
                queue.extend([neig for neig in eqv[j] if cc[neig]!=i])
    return len(set(cc))


while True:
    try: 
        n, m = (int(v) for v in input().split(' '))
    except: break
    img = [[c=='.' for c in input()] for i in range(n)]
    print(ncc(img, n, m))