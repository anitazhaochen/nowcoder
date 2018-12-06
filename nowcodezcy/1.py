#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def solution(line1=None, line2=None):


    all = line1[2] * line1[0]
    c = 0
    for row in line2:
        c += row[0]

    need = all - c

    needtime = 0

    line2.sort(key=lambda x:x[1])
    for row in line2:
        while row[0] < line1[1]:
            if need == 0:
                return needtime
            need -= 1
            needtime += row[1]
            row[0] += 1

    return needtime



if __name__ == "__main__":

    all = []
    line = sys.stdin.readline()
    while line:
        print(line)

        n, r, avg = map(int, line.strip('\n').split(' '))
        score = n * avg
        i = 0
        nowsumscore = 0
        course = []
        while i < n:
            i += 1
            nowscore, needtime = map(int,sys.stdin.readline().strip('\n').split(' '))
            nowsumscore += nowscore
            course.append([nowscore, needtime])

        needalltime = 0
        course.sort(key=lambda x:x[1])
        if nowsumscore < score:
            for everycourse in course:
                while everycourse[0] < r and nowsumscore < score:
                    nowsumscore += 1
                    needalltime += everycourse[1]
                    everycourse[0] += 1
                if nowsumscore == score:
                    print(needalltime)
                    break
        else:
            print(0)
        line = sys.stdin.readline()

