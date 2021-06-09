#!/usr/bin/env python3
# coding: utf8
import os, curses
try:
    stdscr = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.addstr('RED', curses.A_REVERSE | curses.color_pair(1))
    stdscr.getkey()
except Exception as e: raise
finally:
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

