#!/usr/bin/env python
#! -*- coding:utf-8 -*-

"""
Test of task 

Test of all Task class
"""

import pytest
import os.path
import pygs
import json
from pygs.task import TaskManager, Task

__author__ = "Paweł Siergiejuk"
__date__ = "02/11/2019"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"

TEST_JSON_FILE = os.path.join("..", "data", "UT_test.json")


def save_to_test_file(data):
    """Save to test file"""
    file_ = open(TEST_JSON_FILE, "w")
    file_.write(data)
    file_.close()

def test_get_active_task():
    """Test of returning active task"""
    task_data = json.dums({"name": "1",
                           "desc": "2",
                           "value": 3,
                           "id" : 4,
                           "category": "5",
                           "level": 6,
                        })
    save_to_test_file("""{"ACTIVE_TASK":%s}""" % task_data)
    tmg = TaskManager(TEST_JSON_FILE)
    task_1 = Task(json.loads(task_data))
    task_2 = tmg.get_current_task()
    assert task_1.id == task_2.id
    assert task_1.name == task_2.name
    assert task_1.desc == task_2.desc
    assert task_1.value == task_2.value
    assert task_1.category == task_2.category
    assert task_1.level == task_2.level
    
    


if __name__ == "__main__":
    sys.exit()


