#!/usr/bin/env python3
# coding: utf8
import os, curses

class Main:
    def __init__(self, screen, msg):
        self.__screen = screen
        self.__msg = msg
        self.__draw()
        self.__input()
    def __draw(self):
        self.__screen.addstr(self.__msg)
    def __input(self):
        self.__screen.getkey()


if __name__ == "__main__":
    curses.wrapper(Main, 'Hello')

