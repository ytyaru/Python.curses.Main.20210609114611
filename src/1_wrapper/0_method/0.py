#!/usr/bin/env python3
# coding: utf8
import os, curses

def main(stdscr): pass

if __name__ == "__main__":
    os.environ['TERM'] = 'xterm-256color'
    curses.wrapper(main)

