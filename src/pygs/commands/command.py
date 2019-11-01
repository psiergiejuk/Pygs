#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""
General Command class 
"""

import sys
from os.path import join
from pygs.user_status import UserStatus

__author__ = "Paweł Siergiejuk"
__date__ = "28/10/2019"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"


class  Command:
    USER_STATUS_FILE = join("data", "user.json")

    def __init__(self):
        self.status = None

    def execute(self, option):
        """Method that execute command"""
        self.status = self.read_status()
        pass
        self.save_status()
        pass

    def read_status(self):
        """Method that read current user status from the file"""
        return UserStatus(self.USER_STATUS_FILE)

    def save_status(self):
        """Method that save current user status to the file"""
