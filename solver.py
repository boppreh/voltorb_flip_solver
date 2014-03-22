class Board(object):
    def __init__(self, cells=None, rows=None, columns=None):
        self.cells = cells or [set((0, 1, 2, 3)) for i in range(5 * 5)]
        self.rows = rows or []
        self.columns = columns or []

    def __getitem__(self, index):
        x, y = index
        return self.cells[x + y * 5]

    def __setitem__(self, index, value):
        x, y = index
        self.cells[x + y * 5] = value

    def _get_possible_values(self, cell_total, n_bombs):
        numbers_count = 5 - n_bombs
        max_number = cell_total - numbers_count + 1
        possible_values = set(range(1, max_number + 1))
        if n_bombs > 0:
            possible_values.add(0)
        return possible_values

    def update_constraints(self):
        for y, row in enumerate(self.rows):
            for x in range(0, 5):
                self[x, y] &= self._get_possible_values(*row)

        for x, column in enumerate(self.columns):
            for y in range(0, 5):
                self[x, y] &= self._get_possible_values(*column)

    def __repr__(self):
        result = []
        for y in range(5):
            for x in range(5):
                str_cell = ''.join(map(str, sorted(self[x, y])))
                result.append('{0:4} '.format(str_cell))
            result.append('\n')
        return ''.join(result)

if __name__ == '__main__':
    b = Board(rows=[(6, 1), (5, 0), (5, 1), (3, 3), (5, 2)],
              columns=[(5, 1), (6, 1), (5, 2), (3, 2), (5, 1)])
    b.update_constraints()
    print(b[1, 1])
    print(b)

