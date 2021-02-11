import numpy as np
from scipy.stats import norm as Normal
from dataclasses import dataclass

from myterial import salmon_light, salmon, teal, indigo_light

from demo import plot

@dataclass
class GaussianPlottingParameters:
    label: str = None
    label_side: str = 'right'

    mark_mu: bool = True
    mu_label: str = None

    color: str = salmon_light
    plot_shaded: bool = True

    outline_width=1
    lw=4


class Gaussian(GaussianPlottingParameters):
    xrange = [0.0001, 0.9999]

    def __init__(self, mu=0, sigma=1, **kwargs):
        self.mu = mu
        self.sigma = sigma

        # override defaults
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __mul__(self, other):
        mu_one, sigma_one = self.mu, self.sigma
        mu_two, sigma_two = other.mu, other.sigma

        mu = (
                (mu_one / sigma_one ** 2) + (mu_two / sigma_two ** 2)
            ) /  (
                (1 / sigma_one ** 2) + (1 / sigma_two ** 2)
            )

        sigma = 1 /  (
                (1 / sigma_one ** 2) + (1 / sigma_two ** 2)
            )

        return Gaussian(mu=mu, sigma=sigma)
    
    @property
    def distribution(self):
        return Normal(self.mu, self.sigma)

    @property
    def support(self):
        dist = self.distribution
        return np.linspace(dist.ppf(self.xrange[0]), dist.ppf(self.xrange[1]), 500)

    @property
    def pdf(self):
        return self.distribution.pdf(self.support)

    @property
    def peak(self):
        '''
            Value at the mean
        '''
        return self.distribution.pdf(self.mu)


    def draw(self, ax):
        # plot shaded area
        if self.plot_shaded:
            ax.fill_between(
                self.support,
                0.00175,  # to avoid covering x axis
                self.pdf,
                alpha=.3,
                color=self.color,
                zorder=5,
            )

        # plot outline
        plot.elements.plot_line_outlined(
            ax,
            self.support, 
            self.pdf, 
            color=self.color, 
            lw=self.lw, 
            outline=self.outline_width
            )

        # mark mean
        if self.mark_mu:
            plot.elements.vline_to_point(
                ax,
                self.mu,
                self.peak,
                mark_bottom=True,
                color=plot.utils.darken_color(self.color),
                lw=2,
                zorder=3,
                ls='--'
            )

        # label mu
        if self.mu_label is not None:
            plot.elements.label_point(
                ax,
                self.mu,
                0,
                self.mu_label,
                below=True,
                color=plot.utils.darken_color(self.color, .3),
            )

        # label
        if self.label is not None:
            plot.elements.label_point(
                ax,
                self.mu,
                self.peak,
                self.label,
                right=True if self.label_side == 'left' else False,
                color=plot.utils.darken_color(self.color, .3),
            )

class Prior(Gaussian):
    def __init__(self, mu=0, sigma=1, **kwargs):
        Gaussian.__init__(self, mu=mu, sigma=sigma, **kwargs)
        self.color = salmon
        self.label='prior:  $p_s(S_{hyp})$'

class Likelihood(Gaussian):
    def __init__(self, mu=0, sigma=1, **kwargs):
        Gaussian.__init__(self, mu=mu, sigma=sigma, **kwargs)
        self.color = teal
        self.label='likelihood:\n  $L(S_{hyp})=p_{x|s}(X_{obs}|S_{hyp})$'
        self.mu_label='$X_{obs}$'

class Posterior(Gaussian):
    def __init__(self, mu=0, sigma=1, **kwargs):
        Gaussian.__init__(self, mu=mu, sigma=sigma, **kwargs)
        self.color = indigo_light
        self.label = 'posterior:\n  $p_{s|x}(S_{hyp} | X_{obs})$'  # specify label
        self.mu_label = '$\\hat{S}_{PM}$'  # label x=mu in plot