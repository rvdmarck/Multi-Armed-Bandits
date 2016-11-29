import numpy as np
import matplotlib.pyplot as plt


class Plotter():
    def __init__(self, values):
        legends = ["Random", "\epsilon-greedy 0", "\epsilon-greedy 0.1", "\epsilon-greedy 0.2"]
        for i in range(len(values)):
            plt.plot(values[i], label = legends[i])
        plt.legend(loc = 'best')
        plt.show()