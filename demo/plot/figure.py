import matplotlib.pyplot as plt

from demo import plot
from demo.gaussian import Gaussian

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
                # plot shaded area
                self.ax.fill_between(
                    obj.support,
                    0,
                    obj.pdf,
                    alpha=.3,
                    color=obj.color,
                    zorder=5,
                )

                # plot outline
                plot.elements.plot_line_outlined(
                    self.ax,
                    obj.support, 
                    obj.pdf, 
                    color=obj.color, 
                    lw=2, 
                    )

                # mark mean and add label
                plot.elements.vline_to_point(
                    self.ax,
                    obj.mu,
                    obj.peak,
                    mark_bottom=True,
                    color=plot.utils.darken_color(obj.color),
                    lw=4,
                    zorder=3,
                )

                if obj.mu_label is not None:
                    plot.elements.label_point(
                        self.ax,
                        obj.mu,
                        0,
                        obj.mu_label,
                        below=True,
                        color=plot.utils.darken_color(obj.color, .3),
                    )

                if obj.label is not None:
                    self.ax.text(
                        obj.mu + .02,
                        obj.peak + .01,
                        obj.label,
                        horizontalalignment='left',
                        fontsize=14,
                        fontweight='bold',
                        color=plot.utils.darken_color(obj.color, .3),
                    )
                
            else:
                raise NotImplementedError


    def show(self):
        ''' clean up and show figure '''
        plot.utils.clean_axes(self.fig)
        plot.utils.make_axes_at_center(self.ax)
        plt.show()