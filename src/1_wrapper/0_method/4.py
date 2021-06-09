#!/usr/bin/env python3
# coding: utf8
import os, curses

def main(stdscr, msg, color_index=1):
    def init_color_pair():
        if not curses.has_colors(): raise Exception('このターミナルは色を表示できません。')
        if not curses.can_change_color(): raise Exception('このターミナルは色を変更できません。')
        curses.use_default_colors()
        for i in range(1, curses.COLORS):
            curses.init_pair(i, i, curses.COLOR_BLACK)
    def draw():
        try:
            for i in range(1, curses.COLORS):
                stdscr.addstr(str(i).rjust(3), curses.A_REVERSE | curses.color_pair(i))
        except curses.ERR: pass
        stdscr.addstr(7, 0, msg, curses.A_REVERSE | curses.color_pair(color_index))
    init_color_pair()
    draw()
    stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(main, 'Hello', color_index=2)

