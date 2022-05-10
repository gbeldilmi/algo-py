class Sudoku:
    def __init__(self):
        self.grid = [ [ 0 for i in range(9) ] for j in range(9) ]

    def __str__(self):
        s = ''
        for i in range(9):
            for j in range(9):
                s += str(self.grid[i][j]) + ' '
            s += '\n'
        return s

    def empty(self):
        return [ (r,c) for r , row in enumerate(self.grid) for c, val in enumerate(row) if val == 0 ]

    def available(self, x, y):
        row = [ i for i in self.grid[x] ]
        col = [ r[y] for r in self.grid ]
        squ = [ self.grid[i][j] for i in range(x // 3 * 3, x // 3 * 3 + 3) for j in range(y // 3 * 3, y // 3 * 3 + 3) ]
        return set(range(1, 10)) - set(row) - set(col) - set(squ)

    def solve(self):
        e = self.empty()
        if len(e) == 0:
            return self
        x, y = e[0]
        for i in self.available(x, y):
            self.grid[x][y] = i
            if self.solve():
                return self
        self.grid[x][y] = 0
        return None


if __name__ == '__main__':
    s = Sudoku()
    s.grid = [
        [ 5, 0, 6, 0, 0, 8, 1, 0, 0 ],
        [ 0, 1, 0, 0, 9, 2, 8, 0, 0 ],
        [ 0, 0, 0, 1, 0, 0, 0, 0, 3 ],
        [ 0, 0, 0, 2, 0, 4, 0, 0, 0 ],
        [ 0, 8, 2, 0, 0, 1, 0, 0, 6 ],
        [ 1, 0, 0, 0, 0, 0, 3, 0, 7 ],
        [ 0, 0, 8, 0, 4, 5, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 6, 9, 0, 8 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    ]
    print(s)
    if s.solve():
        print(s)
    else:
        print('No solution')
