#!/usr/bin/env python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def mean(data):
    return sum(data)/len(data)


def loadTxt(filename):
    dataset = []
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        dataset.append(line.split("\t")[0:7])
    del dataset[0]

    for i in range(0, len(dataset)):
        try:
            for j in range(len(dataset[i])):
                if j == 0:
                    dataset[i][j] = int(float(dataset[i][j]))
                else:
                    dataset[i][j] = float(dataset[i][j])
        except ValueError, e:
            print "ValueError at %d" % i
    f.close()
    return dataset
def detect(dataset, T):
    state = []
    for i in range(5, len(dataset)):
        delta = (dataset[i, 1] - mean(dataset[i-5:i, 1]), dataset[i, 2] - mean(dataset[i-5:i, 2]), dataset[i, 3] - mean(dataset[i-5:i, 3]))
        if max(delta) > T:
            state.append(1)
        else:
            state.append(0)

    return state


if __name__ == "__main__":

    dataset = loadTxt("pengzhuang/pz1.txt")
    data = np.array(dataset)
    state = detect(data, 4)

    plt.figure(1, figsize=(10,10))
    plt.plot(range(len(data)), data[:, 1])
    plt.plot(range(len(data)), data[:, 2])
    plt.plot(range(len(data)), data[:, 3])
    # for s in state:
    #     if s[0] == 1:
    #         print s
    plt.figure(2, figsize=(10, 10))
    plt.plot(range(len(state)), state, 'r.')
    plt.ylim(-1, 2)
    plt.legend()
    plt.show()
