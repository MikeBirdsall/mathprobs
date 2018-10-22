#! /usr/bin/python3

""" Program to determine the chances of having a seventh son in a family of
    particular size. starting with 7 and going up, say, to 20.
"""


count_ = [0]*21
prob = [0]*21
for kids in range(7, 21):
    count_[kids] = 0
    for x in range(2**kids):
        if bin(x).count("1") >= 7:
            count_[kids] += 1
    prob[kids] = count_[kids] / 2 ** kids
    print("{} combinations of {} kids with 7 or more sons, prob={}".format(
        count_[kids], kids, prob[kids])
    )





