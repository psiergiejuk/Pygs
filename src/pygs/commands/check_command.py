#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""
Check Command class 

It is use to check the current user solution
"""

import sys
from pygs.commands import Command

__author__ = "Paweł Siergiejuk"
__date__ = "27/10/2019"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"


class CheckCommand(Command):

    def execute(self, option):
        """Method that execute command"""
        print("Test ", option)
