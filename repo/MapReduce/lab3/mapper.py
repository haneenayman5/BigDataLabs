#!/usr/bin/env python3

import sys


for line in sys.stdin:

    line = line.strip()


    if not line:
        continue


    parts = line.split()


    ip = parts[0]


    print(f"{ip}\t1")
