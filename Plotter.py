import numpy as np
import matplotlib.pyplot as plt



def Plotter1(values):
    legends = ["Random", "e-greedy 0", "e-greedy 0.1", "e-greedy 0.2", "softmax-1", "softmax-0.1"]
    for i in range(len(values)):
        plt.plot(values[i], label = legends[i])
    plt.legend(loc = 'best')
    plt.show()

def Plotter2(values):
    legends = ["Q*", "Q_Random", "Q_greedy0", "Q_greedy0.1", "Q_greedy0.2", "Qsoftmax-1", "Qsoftmax-0.1"]
    for i in range(len(values)):
        plt.plot(values[i], label=legends[i])
    plt.legend(loc='best')
    plt.show()

def Plotter3(values):
    plt.hist(values)
    plt.show()

def Plotter4(values):
    legends = ["Random", "e-greedy 0", "e-greedy 0.1", "e-greedy 0.2", "e-greedy var", "softmax-1", "softmax-0.1", "softmax var"]
    for i in range(len(values)):
        plt.plot(values[i], label = legends[i])
        plt.plot(values[i])
    plt.legend(loc = 'best')
    plt.show()

def Plotter5(values):
    legends = ["Q*", "Q_Random", "Q_greedy0", "Q_greedy0.1", "Q_greedy0.2","Q_greedyVar", "Qsoftmax-1", "Qsoftmax-0.1", "QsoftmaxVar"]
    for i in range(len(values)):
        plt.plot(values[i], label=legends[i])
    plt.legend(loc='best')
    plt.show()