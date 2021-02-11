from demo import Gaussian, Prior, Likelihood, Posterior, Figure


# create prior and likelihood distributions
prior = Prior(
    mu=0, sigma=2.5, 
    mark_mu=False, label_side='right'
)

likelihood = Likelihood(
    mu=4, sigma=1, 
)

# compute posterior's mean and standard deviation
posterior_mu = (
        (prior.mu / prior.sigma ** 2) + (likelihood.mu / likelihood.sigma ** 2)
    ) / (
        (1 / prior.sigma ** 2) + (1 / likelihood.sigma ** 2)
    )

posterior_sigma = (
        1 
    ) / (
        (1 / prior.sigma ** 2) + (1 / likelihood.sigma ** 2)
    )

# create a 'poterior' object for plotting
posterior = Posterior(
    mu=posterior_mu,
    sigma=posterior_sigma,
    mu_label_side = 'right'
)

# create a figure
figure = Figure(
    title='Fig. 3.5',
    xlabel='Hypothesized stimulus $S_{hyp}$',
    ylabel="Probability or likelihood",
)

# add elements to plot
figure.add(prior, likelihood, posterior)

# show figure
figure.show()
figure.save('demo.png')
