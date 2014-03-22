class Board(object):
    def __init__(self, cells=None, rows=None, columns=None):
        self.cells = cells or [set((0, 1, 2, 3)) for i in range(5 * 5)]
        self.rows = rows or []
        self.columns = columns or []

    def __getitem__(self, index):
        x, y = index
        return self.cells[x + y * 5]

    def update_cnstraints(self):
        pass

if __name__ == '__main__':
    b = Board(rows=[(6, 1), (5, 0), (5, 1), (3, 3), (5, 2)],
              columns=[(5, 1), (6, 1), (5, 2), (3, 2), (5, 1)])
    print(b[1, 1])

