


try:
    while True:
        n = int(input())
        emails = [input().split('@') for i in range(n)]
        emails = [[e[0].replace('.', '').split('+', 1)[0], e[1]] for e in emails]
        emails = [e[0] + '@' + e[1] for e in emails]
        print(len(set(emails)))
except EOFError:
    pass