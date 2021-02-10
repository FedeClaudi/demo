from demo import plot

def plot_line_outlined(
    ax, x, y=None, lw=4, outline=2, outline_color=[.3, .3, .3], color="r", **kwargs
):
    '''
        Plots a line with a darker outline around it
    '''
    if y is not None:
        ax.plot(x, y, lw=lw + outline, color=outline_color, solid_capstyle='round', zorder=9)
        ax.plot(x, y, lw=lw, color=color, zorder=10, solid_capstyle='round', **kwargs)
    else:
        ax.plot(x, lw=lw + outline, color=outline_color, solid_capstyle='round', zorder=9)
        ax.plot(x, lw=lw, color=color, zorder=10, solid_capstyle='round', **kwargs)



def vline_to_point(ax, x, y, ymin=0, mark_bottom=False, mark_top=False, color='k', zorder=8, **kwargs):
    ax.plot([x, x], [ymin, y], color=color, zorder=zorder, solid_capstyle='round', **kwargs)

    if mark_bottom:
        ax.scatter(x, ymin, s=100, edgecolors=[.3, .3, .3], lw=1, zorder=8, color=color)

    if mark_top:
        ax.scatter(x, y, s=100, edgecolors=[.3, .3, .3], lw=1, zorder=8, color=color)


def label_point(ax, x, y, text, below=False, right=False, color='k'):
    '''
        Add some text to label a point
    '''
    xshift = .025 if not right else -.025
    yshift = .005 if not below else -.005
    ax.text(
        x + xshift,
        y + yshift,
        text,
        horizontalalignment='left' if not right else 'right',
        verticalalignment='bottom' if not below else 'top',
        fontsize=14,
        fontweight='bold',
        color=color,
    )