from cell import cell
import dead

class alive(cell):
    def __init__(self, left, top, width, height):
        super().__init__(left, top, width, height)

    def stay(self, block_list):
        counter = 0
        for block in block_list:
            if (block.get_rect().left == self.rect.left or
                    block.get_rect().top == self.rect.top and isinstance(block, alive)):
                counter += 1
        return counter > 3

        counter = 0
        for block in block_list:
            if (block.get_rect().left == self.rect.left or
                    block.get_rect().top == self.rect.top and isinstance(block, dead.dead)):
                counter += 1
        return counter > 2

        return True
