#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

for line in sys.stdin:
    n, r, avg = line.rstrip().split()
    n = int(n)
    r = int(r)
    avg = int(avg)
    target = n * avg
    course = []
    for i in range(n):
        line = sys.stdin.next().rstrip().split()
        target -= int(line[0])
        course.append((r - int(line[0]), int(line[1])))
    course.sort(key=lambda x: x[1], reverse=False)

    course_id = 0
    ret = 0
    while target > 0 and course_id < n - 1:
        if target >= course[course_id][0]:
            target -= course[course_id][0]
            ret += course[course_id][0] * course[course_id][1]
        else:
            ret += target * course[course_id][1]
            break
        course_id += 1
    print ret