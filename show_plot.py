from demo import Prior, Likelihood, Posterior, Figure


# create prior and likelihood distributions
prior = Prior(
    mu=0, sigma=2.5, 
    mark_mu=False, label_side='left'
)

likelihood = Likelihood(
    mu=3.8, sigma=1, 
)

# compute posterior by multiplying the two
posterior = Posterior(prior * likelihood)

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
