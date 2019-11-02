#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""
PyGS

Python Game System

Main file of the project
"""

import sys
import argparse

from pygs.commands import TaskComamnd, CheckCommand, NextCommand, ResultCommand

__author__ = "Paweł Siergiejuk"
__date__ = "02/11/2019"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"


ACTION = {
          "task": TaskComamnd(),
          "check": CheckCommand(),
          "next": NextCommand(),
          "result": ResultCommand(),
          }

def main():
    parser = argparse.ArgumentParser(description="Python Game System")
    parser.add_argument("command", type=str, choices=ACTION.keys(), help="Command type")
    parser.add_argument("option", type=str, nargs="?", default="", help="Additional option for command")
    args  = parser.parse_args()
    ACTION[args.command].execute(args.option)


if __name__ == "__main__":
    main()


