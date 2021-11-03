from Cell import Cell


class Node:
    initial_position_counter = 0

    def __init__(self, cell_type: Cell, x: int, y: int):
        self.cell_type = cell_type
        self.x = x
        self.y = y
        self.number = None
        if cell_type is Cell.INITIAL_POS:
            Node.initial_position_counter += 1
            self.number = Node.initial_position_counter

    def __str__(self):
        return f"{self.cell_type} {self.number} ({self.x}, {self.y})"