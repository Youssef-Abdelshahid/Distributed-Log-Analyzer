#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) != 4:
        continue
    _, node, ip, status = parts
    try:
        status = int(status)
    except ValueError:
        continue

    print(f"TOTAL\t1")
    if status >= 400:
        print(f"ERROR\t1")
    print(f"NODE_{node}\t1")
    print(f"IP_{ip}\t1")
