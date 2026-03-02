#!/usr/bin/env python3
"""
Minimal console-based Snake game using curses.

This implementation uses only the Python standard library. On Windows
install the `windows-curses` package if the built-in curses module is
not available:

    pip install windows-curses

Run this script from a terminal and play using the arrow keys.
"""

import curses
import random
import time


def main(stdscr):
    # configure curses
    curses.curs_set(0)  # hide cursor
    stdscr.nodelay(True)  # non-blocking input
    stdscr.keypad(True)  # capture special keys

    # window size
    height, width = stdscr.getmaxyx()

    # initial snake (middle of screen, 3 segments)
    snake = [
        (height // 2, width // 2 + i)
        for i in range(3)
    ]
    direction = curses.KEY_LEFT

    # place initial food
    food = None

    def place_food():
        nonlocal food
        while True:
            pos = (
                random.randint(1, height - 2),
                random.randint(1, width - 2),
            )
            if pos not in snake:
                food = pos
                break

    place_food()

    score = 0
    delay = 0.1

    while True:
        # input handling
        try:
            key = stdscr.getch()
        except curses.error:
            key = -1

        if key in (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT):
            # don't reverse direction directly
            opposite = {curses.KEY_UP: curses.KEY_DOWN,
                        curses.KEY_DOWN: curses.KEY_UP,
                        curses.KEY_LEFT: curses.KEY_RIGHT,
                        curses.KEY_RIGHT: curses.KEY_LEFT}
            if key != opposite.get(direction, None):
                direction = key

        # compute new head
        head_y, head_x = snake[0]
        if direction == curses.KEY_UP:
            head_y -= 1
        elif direction == curses.KEY_DOWN:
            head_y += 1
        elif direction == curses.KEY_LEFT:
            head_x -= 1
        elif direction == curses.KEY_RIGHT:
            head_x += 1

        new_head = (head_y, head_x)

        # check collisions with wall or self
        if (
            head_y < 0 or head_y >= height
            or head_x < 0 or head_x >= width
            or new_head in snake
        ):
            break  # game over

        snake.insert(0, new_head)

        # check food
        if new_head == food:
            score += 1
            place_food()
            # optionally increase speed
            delay = max(0.02, delay * 0.9)
        else:
            snake.pop()  # remove tail

        # draw
        stdscr.clear()
        stdscr.addstr(0, 2, f"Score: {score}")
        stdscr.addch(food[0], food[1], "*")
        for y, x in snake:
            stdscr.addch(y, x, "#")
        stdscr.refresh()

        time.sleep(delay)

    # game over message
    stdscr.nodelay(False)
    stdscr.clear()
    stdscr.addstr(height // 2, width // 2 - 5, "GAME OVER")
    stdscr.addstr(height // 2 + 1, width // 2 - 7, f"Final score: {score}")
    stdscr.addstr(height // 2 + 3, width // 2 - 12, "Press any key to exit")
    stdscr.refresh()
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
