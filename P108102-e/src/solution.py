from typing import NamedTuple


class Minion(NamedTuple):
    name: str
    hunger: int
    motivation: int
    size: str


def from_line(line: str) -> Minion:
    tokens = line.strip("\n").split(";")
    return Minion(tokens[0], int(tokens[1]), int(tokens[2]), tokens[3])


def to_line(minion: Minion) -> str:
    return f"{minion.name} {minion.hunger} ({minion.size})"


def order(minions: list[Minion]) -> list[Minion]:
    return sorted(minions, key=lambda minion: (-minion.motivation, minion.name))
