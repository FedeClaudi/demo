import matplotlib.pyplot as plt

from demo import plot
from demo.gaussian import Gaussian, plot_gaussian

class Figure():
    def __init__(self, title=None, xlabel='', ylabel='', show_y_ticks=False):
        '''
            Represents a figure.
        '''
        # create figure
        self.fig, self.ax = plt.subplots(figsize=(12, 9))

        if title is not None:
            self.fig.suptitle(title)

        # set up axis labels
        self.ax.set(xlabel=xlabel, ylabel=ylabel)

        if not show_y_ticks:
            self.ax.set(yticks=[])


    def add(self, *objs):
        '''
            Add objects (e.g. gaussian distributions).
        '''
        for obj in objs:
            if isinstance(obj, Gaussian):
                plot_gaussian(obj, self.ax)
            else:
                raise NotImplementedError


    def show(self):
        ''' clean up and show figure '''
        plot.utils.clean_axes(self.fig)
        plot.utils.make_axes_at_center(self.ax)
        plt.show()

    def save(self, path):
        self.fig.savefig(str(path))