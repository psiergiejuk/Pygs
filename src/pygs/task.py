#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""
Task Class

Class that handle the task operation
"""

import sys
import json

__author__ = "Paweł Siergiejuk"
__date__ = "02/11/2019"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"

class Task():
    """Object that handle all Task data"""
    
    def __init__(self, active_data):
        self.active_data = active_data


class TaskManager():
    """Class Task that handle active task"""
    ACTIVE = "ACTIVE_TASK"
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = json.load(open(json_file))
        self.active = Task(self.data[self.ACTIVE])

    def get_current_task(self):
        """Method that return current active task"""
        return self.active()

if __name__ == "__main__":
    sys.exit()


