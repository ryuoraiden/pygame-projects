# pygame-projects

Small Pygame games I made while learning the library. Some of it I wrote myself and some follows a tutorial closely, so this is a study repo, not original work. I keep it around to reread when I start my own games.

## Files

| File | What it shows |
|---|---|
| `window_template.py` | The bare minimum: open a window, run the event loop, quit. Copy it to start a new game. |
| `square_game.py` | Keyboard movement with `Rect`, a bouncing enemy, collision checks, a score counter and a game-over screen. |
| `rocket_shooter.py` | Two-player shooter. Loading, scaling and rotating sprites, playing sounds, keeping bullets in lists, and custom `USEREVENT`s for hits. |

## Credit

`rocket_shooter.py` is based on Tech With Tim's [PygameForBeginners](https://github.com/techwithtim/PygameForBeginners) tutorial, and everything in `Assets/` comes from that repo. My version changes the window size, ship size, speeds, bullet limit and fonts, and turns the sounds on.

## Run

```bash
pip install -r requirements.txt
python rocket_shooter.py
```

Run it from this folder, since the games load `Assets/` with a relative path.

**Rocket Shooter:** yellow moves with WASD and fires with Left Shift, red moves with the arrow keys and fires with Right Shift.
**Square Game:** move with WASD, grab the green square, stay away from the red one.

## Things to fix next time

- Closing the Rocket Shooter window mid-game can crash with `video system not initialized`. `pygame.quit()` runs inside the event loop, and the rest of that frame still calls Pygame.
- `handle_bullets` removes bullets from a list while looping over that same list, which can skip the next bullet.
- Restarting after a win calls `main()` from inside `main()`, so every round adds another frame to the call stack.
- Square Game moves in one direction at a time because of the `elif` chain, and the enemy can spawn right on top of the player.
- Square Game has no restart key, so game over is a dead end.
