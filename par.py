def toggle(grid,n):
    if n < len(grid):
        for i in range(len(grid)):
            grid[n][i] = 1-grid[n][i]
    else:
        for i in range(len(grid)):
            grid[i][n-len(grid)] = 1-grid[i][n-len(grid)]

def mostZeros(grid):
    n = len(grid)

    maxi = 0
    imaxi = 0
    for i in range(n):
        nb = 0
        for cur in grid[i]:
            if cur == 0:
                nb += 1
        if nb >= maxi:
            maxi = nb
            imaxi = i
    for i in range(n):
        nb = 0
        for j in range(n):
            cur = grid[j][i]
            if cur == 0:
                nb += 1
        if nb >= maxi:
            maxi = nb
            imaxi = i+n

    return imaxi


def solveToggle(g):
    i = 0
    l = []
    while zeroInGrid(g) and i < 1000:
        i+=1
        l.append(mostZeros(g))
        toggle(g, l[-1])
    return l

def zeroInGrid(g):
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] == 0:
                return True
    return False

