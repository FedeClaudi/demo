import matplotlib.pyplot as plt

from demo._plot import clean_axes
from demo.gaussian import Gaussian

class Figure():
    def __init__(self, title=None):
        self.fig, self.ax = plt.subplots(figsize=(12, 9))
        clean_axes(self.fig)

        if title is not None:
            self.fig.suptitle(title)


    def add(self, *objs):
        for obj in objs:
            if isinstance(obj, Gaussian):
                # plot shaded area
                self.ax.fill_between(
                    obj.support,
                    0,
                    obj.pdf,
                    alpha=.2,
                    color=obj.color,
                )

                # plot outline
                self.ax.plot(obj.support, obj.pdf, color=obj.color, lw=2, alpha=1)
            else:
                raise NotImplementedError

    def show(self):
        plt.show()