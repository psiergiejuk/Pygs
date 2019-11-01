#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""Package that handle all commands"""

import sys
from pygs.commands.command import Command
from pygs.commands.next_command import NextCommand
from pygs.commands.check_command import CheckCommand
from pygs.commands.task_command import TaskComamnd
from pygs.commands.result_command import ResultCommand

__author__ = "Paweł Siergiejuk"
__date__ = "27/10/2019"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"


__slots__ = ["Command", "NextCommand", "CheckCommand", "TaskComamnd", "ResultCommand"]

