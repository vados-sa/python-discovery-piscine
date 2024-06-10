#!/usr/bin/env python3

import sys
import re

if len(sys.argv) <= 2:
    print("none")
else:
    found = re.findall(sys.argv[1], sys.argv[2])
    x = len(found)
    print(x if x > 0 else "none")
