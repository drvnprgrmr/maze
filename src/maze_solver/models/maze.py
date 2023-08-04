from dataclasses import dataclass
from functools import cached_property
from typing import Iterator

from maze_solver.models.role import Role
from maze_solver.models.border import Border
from maze_solver.models.square import Square


@dataclass(frozen=True)
class Maze:
    squares: tuple[Square, ...]

    def __post_init__(self) -> None:
        validate_indices(self)
        validate_rows_columns(self)
        validate_entrance(self)
        validate_exit(self)

    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

    def __getitem__(self, index: int) -> Square:
        return self.squares[index]

    @cached_property
    def width(self) -> int:
        return max(square.column for square in self) + 1

    @cached_property
    def height(self) -> int:
        return max(square.row for square in self) + 1
    
    @cached_property
    def entrance(self) -> Square:
        return next(square for square in self if square.role is Role.ENTRANCE)
    
    @cached_property
    def exit(self) -> Square:
        return next(square for square in self if square.role is Role.EXIT)


def validate_indices(maze: Maze) -> None:
    assert [square.index for square in maze] == list(
        range(len(maze.squares))
    ), "Wrong square.index"


def validate_rows_columns(maze: Maze) -> None:
    for y in range(maze.height):
        for x in range(maze.width):
            square = maze[y * maze.width + x]
            assert square.row == y, "Wrong square.row"
            assert square.column == x, "Wrong square.column"


def validate_entrance(maze: Maze) -> None:
    assert [square.role for square in maze].count(
        Role.ENTRANCE
    ) == 1, "Must be exactly one entrance"


def validate_exit(maze: Maze) -> None:
    assert [square.role for square in maze].count(
        Role.EXIT
    ) == 1, "Must be exactly one exit"



if __name__ == "__main__":
    # Create a sample maze
    maze = Maze(
        squares=(
            Square(0, 0, 0, Border.TOP | Border.LEFT),
            Square(1, 0, 1, Border.TOP | Border.RIGHT),
            Square(2, 0, 2, Border.LEFT | Border.RIGHT, Role.EXIT),
            Square(3, 0, 3, Border.TOP | Border.LEFT | Border.RIGHT),
            Square(4, 1, 0, Border.BOTTOM | Border.LEFT | Border.RIGHT),
            Square(5, 1, 1, Border.LEFT | Border.RIGHT),
            Square(6, 1, 2, Border.BOTTOM | Border.LEFT),
            Square(7, 1, 3, Border.RIGHT),
            Square(8, 2, 0, Border.TOP | Border.LEFT, Role.ENTRANCE),
            Square(9, 2, 1, Border.BOTTOM),
            Square(10, 2, 2, Border.TOP | Border.BOTTOM),
            Square(11, 2, 3, Border.BOTTOM | Border.RIGHT),
        )
    )