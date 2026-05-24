#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split('***')

    if len(parts) < 2:
        continue

    try:
        score = float(parts[0])

        region_city = parts[1]

        # Example: China_Beijing
        city = region_city.split('_', 1)[1]

        print(f"{city}\t{score}")

    except (ValueError, IndexError):
        continue

