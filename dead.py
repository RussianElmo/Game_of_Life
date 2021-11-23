import alive
from cell import cell


class dead(cell):
    def __init__(self, left, top, width, height):
        super().__init__(left, top, width, height)

    def stay(self, block_list):
        counter = 0
        for block in block_list:
            if (block.get_rect().left == self.rect.left or
                    block.get_rect().top == self.rect.top and isinstance(block, alive.alive)):
                counter += 1
        return counter >= 3
