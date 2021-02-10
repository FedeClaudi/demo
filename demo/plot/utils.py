import seaborn as sns

import numpy as np
from colormap import rgb2hex, rgb2hls, hls2rgb


def hex_to_rgb(hex):
     hex = hex.lstrip('#')
     hlen = len(hex)
     return tuple(int(hex[i:i+hlen//3], 16) for i in range(0, hlen, hlen//3))

def adjust_color_lightness(r, g, b, factor):
    h, l, s = rgb2hls(r / 255.0, g / 255.0, b / 255.0)
    l = max(min(l * factor, 1.0), 0.0)
    r, g, b = hls2rgb(h, l, s)
    return rgb2hex(int(r * 255), int(g * 255), int(b * 255))

def darken_color(hex, factor=0.2):
    r, g, b = hex_to_rgb(hex)
    return adjust_color_lightness(r, g, b, 1 - factor)

def clean_axes(f):
    '''
        Clens up a figures axes making them look better
    '''
    ax_list = f.axes

    for ax in list(ax_list):
        try:
            sns.despine(ax=ax, offset=1, trim=True, left=False, right=True)
        except:
            pass


def make_axes_at_center(ax):
    """
        Moves the axes splines to the center instead of the bottom left of the ax
    """
    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines["left"].set_position("zero")

    # Eliminate upper and right axes
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")

    # fix y axis label
    ax.yaxis.set_label_coords(-0.05, 0.5)
    