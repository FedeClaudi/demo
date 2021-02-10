import numpy as np
from scipy.stats import norm as Normal

from myterial import salmon_light

class Gaussian:
    xrange = [0.0001, 0.9999]

    def __init__(self, mu=0, sigma=1, color=salmon_light, label=None, mu_label=None):
        self.mu = mu
        self.sigma = sigma
        self.color = color
        self.label = label
        self.mu_label = mu_label

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