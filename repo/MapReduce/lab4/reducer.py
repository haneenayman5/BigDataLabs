#!/usr/bin/env python3
import sys
import math

current_city = None
scores = []

def calculate_and_print(city, scores):

    count = len(scores)

    mean = sum(scores) / count

    variance = sum((x - mean) ** 2 for x in scores) / count

    std = math.sqrt(variance)

    print(f"{city}\tcount={count}\tmean={round(mean,2)}\tstd={round(std,2)}")


for line in sys.stdin:

    line = line.strip()

    if not line:
        continue

    city, score_str = line.split('\t')

    try:
        score = float(score_str)
    except ValueError:
        continue

    if current_city == city:

        scores.append(score)

    else:

        if current_city is not None:
            calculate_and_print(current_city, scores)

        current_city = city
        scores = [score]


# print last city
if current_city is not None:
    calculate_and_print(current_city, scores)
