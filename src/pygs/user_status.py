#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""
User Status Class

Class that store all information about user
"""

#TODO: all import block
import sys
import json

__author__ = "Paweł Siergiejuk"
__date__ = "28/10/2019"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"


class  UserStatus:
    
    def __init__(self, json_file):
        self.data = json.load(open(json_file))
        print(self.data)


if __name__ == "__main__":
    sys.exit()


