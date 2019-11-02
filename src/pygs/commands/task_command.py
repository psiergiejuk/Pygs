#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""
Task Command class 

It is use to display current task to the user
"""

import sys
from pygs.commands import Command
from pygs.task import ActiveTask

__author__ = "Paweł Siergiejuk"
__date__ = "02/11/2019"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"


class TaskComamnd(Command):

    def execute(self, option):
        """Method that execute command"""
        print("Test")
