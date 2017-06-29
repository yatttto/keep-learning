#!/usr/bin/env python
# encoding: utf-8

import random

red = [_+1 for _ in range(33)]
blue =[_+1 for _ in range(16)]

def getred(red):
    redballs = []
    for _ in range(6):
        ball = random.choice(red)
        red.remove(ball)
        redballs.append(ball)
    redballs.sort()
    return  redballs

def getblue(blue):
    return random.choice(blue)

print (getred(red))
print (getblue(blue))




