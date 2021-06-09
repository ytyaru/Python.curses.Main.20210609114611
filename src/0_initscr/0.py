#!/usr/bin/env python3
# coding: utf8
import os, curses
try:
    os.environ['TERM'] = 'xterm-256color'
    stdscr = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
except Exception as e: raise
finally:
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

