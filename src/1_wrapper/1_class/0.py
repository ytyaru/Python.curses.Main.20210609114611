#!/usr/bin/env python3
# coding: utf8
import os, curses

class Main:
    def __init__(self, screen):
        self.__screen = screen


if __name__ == "__main__":
    curses.wrapper(Main)

