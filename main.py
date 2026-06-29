from __future__ import annotations

import attrs
import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

@attrs.define()
class PlayerState:
    player_x : int
    player_y : int

    def onDraw(self, console: tcod.console.Console) -> None:
        console.print(self.player_x, self.player_y, "@")

    def on_event(self, event: tcod.event.Event) -> None:
        match event:
            case tcod.event.Quit():
                raise SystemExit
            case tcod.event.KeyDown(sym=tcod.event.KeySym.LEFT):
                if(not (self.player_x < 1)):
                    self.player_x -= 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.RIGHT):
                if(not (self.player_x  > SCREEN_WIDTH-2)):
                    self.player_x += 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.UP):
                if(not (self.player_y < 1)):
                    self.player_y -= 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.DOWN):
                if(not (self.player_y > SCREEN_HEIGHT-2)):
                    self.player_y += 1

def main() -> None:
    tileset = tcod.tileset.load_tilesheet(
        "data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )
    tcod.tileset.procedural_block_elements(tileset=tileset) #acc loads the tileset

    console = tcod.console.Console(SCREEN_WIDTH, SCREEN_HEIGHT)
    state = PlayerState(player_x=console.width // 2, player_y=console.height // 2)
    with tcod.context.new(console=console, tileset=tileset) as context:
        while True:
            console.clear()
            state.onDraw(console)
            context.present(console)
            for event in tcod.event.wait():
                print(event)
                state.on_event(event)
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit

if __name__ == "__main__":
    main()