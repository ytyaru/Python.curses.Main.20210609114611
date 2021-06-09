#!/usr/bin/env python3
# coding: utf8
import os, curses
def main(stdscr):
    curses.curs_set(0)
    if not curses.has_colors(): raise Exception('このターミナルは色を表示できません。')
    if not curses.can_change_color(): raise Exception('このターミナルは色を変更できません。')
    curses.use_default_colors()
    for i in range(1, curses.COLORS):
        curses.init_pair(i, i, curses.COLOR_BLACK)
    try:
        for i in range(1, curses.COLORS):
            stdscr.addstr(str(i).rjust(3), curses.A_REVERSE | curses.color_pair(i))
    except curses.ERR: pass
    stdscr.refresh()
    stdscr.getkey()


if __name__ == "__main__":
    try:
        os.environ['TERM'] = 'xterm-256color'
        stdscr = curses.initscr()
        curses.start_color()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        main(stdscr)
    except Exception as e: raise
    finally:
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
