
class Cell:
    _is_live: bool

    def __init__(self):
        pass

    def die(self):
        pass

    def live(self):
        pass


class Board:
    _height: int
    _width: int
    _data: [[Cell]]

    def __init__(self):
        pass

    def next_epoch(self):
        pass

    def random_fill(self):
        pass

    def __calculate_neighbours(self) -> [[int]]:
        pass

    def __calculate_neighbour(self, x: int, y: int) -> int:
        pass


class Game:
    _board: Board
    _epoch_counter: int = 0
    _epoch_limit: int

    def __init__(self):
        pass

    def start(self):
        pass
