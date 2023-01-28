#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'docstring' function below.
#
# The function is expected to output a STRING.
# The function accepts STRING x as parameter.
#

def docstring(functionname:str):
    # Write your code here
    return help(functionname)

if __name__ == '__main__':

    x = input()
    docstring(x)

