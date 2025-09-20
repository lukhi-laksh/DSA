class Spreadsheet:
    def __init__(self, rows):
        # Only store explicitly set cells for O(1) lookup.
        self.cells = {}

    def setCell(self, cell, value):
        self.cells[cell] = value

    def resetCell(self, cell):
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula):
        i = formula.find('+')
        left = formula[1:i]
        right = formula[i+1:]
        return self._get_token(left) + self._get_token(right)

    def _get_token(self, token):
        # Fast digit/cell reference distinction
        return int(token) if token[0].isdigit() else self.cells.get(token, 0)