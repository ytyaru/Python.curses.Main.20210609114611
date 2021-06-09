#!/usr/bin/env python3
# coding: utf8
import os, curses

class Main:
    def __init__(self, screen, msg):
        self.__screen = screen
        self.__msg = msg


if __name__ == "__main__":
    curses.wrapper(Main, 'Hello')

