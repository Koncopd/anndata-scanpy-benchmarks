import matplotlib.pyplot as plt
import numpy as np

def plot_groups(groups, dense, sparse, xlabel, ylabel, title):
    fig, ax = plt.subplots()
    index = np.arange(len(groups))
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, dense, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Dense')

    rects2 = plt.bar(index + bar_width, sparse, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Sparse')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(index + bar_width/2, groups)
    plt.legend()

    plt.tight_layout()
    plt.show()

def simple_bar(xlabels, ylabel, title, data):
    ind = np.arange(len(xlabels))

    plt.figure(figsize=(8, 7))

    plt.bar(ind, data, align='center', alpha=0.5)
    plt.xticks(ind, xlabels)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.show()
