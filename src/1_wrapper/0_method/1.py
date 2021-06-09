#!/usr/bin/env python3
# coding: utf8
import os, curses

def main(stdscr, msg):
    stdscr.addstr(msg)
    stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(main, 'Hello')

