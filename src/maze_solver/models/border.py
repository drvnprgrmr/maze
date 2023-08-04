from enum import IntFlag, auto


class Border(IntFlag):
    EMPTY = 0
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()

    @property
    def corner(self) -> bool:
        """Check if this border forms an edge (i.e. two adjacent borders)"""
        return self in (
            self.TOP | self.LEFT,
            self.TOP | self.RIGHT,
            self.BOTTOM | self.LEFT,
            self.BOTTOM | self.RIGHT,
        )

    @property
    def dead_end(self) -> bool:
        """Check if border forms a dead end"""
        return self.bit_count() == 3
    
    @property
    def intersection(self) -> bool:
        """Check if border arrangement forms an intersection"""
        return self.bit_count() < 2