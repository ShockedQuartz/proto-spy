#Components for the graphics and position of entities
from __future__ import annotations

from typing import Final, Self

import attrs
import tcod.ecs.callbacks
from tcod.ecs import Entity


@attrs.define(frozen=True)
class Position:
    #An entity's position
    x: int
    y: int

    def __add__(self, direction: tuple[int, int]) -> Self:
        x, y = direction
        return self.__class__(self.x + x, self.y + y)

@tcod.ecs.callbacks.register_component_changed(component=Position)
def on_position_changed(entity: Entity, old: Position | None, new: Position | None) -> None:
    if old == new:
        return
    if old is not None:
        entity.tags.discard(old)
    if new is not None:
        entity.tags.add(new)

@attrs.define(frozen=True)
class Graphics:
    ch: int = ord("!")
    fg: tuple[int, int, int] = (255, 255, 255)

Gold: Final = ("Gold", int)
#TEMP, how much gold an entity has