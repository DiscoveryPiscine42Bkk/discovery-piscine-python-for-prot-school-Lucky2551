#!/usr/bin/env python3

import sys

def aff_first_param():
    """Displays the first parameter or 'none' if no parameters are given."""
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("none")

if name == "main":
    aff_first_param()
