#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")

else:
    def downcase_it(str):
        for x in str[1:]:
            print(x.lower())

    downcase_it(sys.argv)