from scipy import ndimage
from random import randint
from colouring_game_scenarios import ncc
from datetime import datetime as dt


nok = 0
while True:
    n = randint(1, 1024)
    m = randint(1, 1024)
    img = [[randint(0, 1)==1 for j in range(m)] for i in range(n)]
    start = dt.now()
    _, true_ncc = ndimage.label(img)
    t1 = dt.now() - start
    start = dt.now()
    pred_ncc = ncc(img, n, m)
    t2 = dt.now() - start
    if true_ncc != pred_ncc:
        print(f"{n} {m}")
        for i in range(n):
            for j in range(m):
                print('.' if img[i][j] else 'o', end='')
            print('')
        break
    else:
        nok+=1
        print(f"{nok} -> {n}\t{m}\t{t1}\t{t2}\t{t2/t1}", flush=True)
