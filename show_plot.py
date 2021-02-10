from demo import Gaussian, Figure, teal, indigo_light


# create prior and likelihood distributoins
prior = Gaussian(mu=0, sigma=3)

likelihood = Gaussian(mu=3.5, sigma=1, color=teal)

# compute posterior
posterior = prior * likelihood
posterior.color = indigo_light  #  specify color

# create and show figure
figure = Figure(title='Fig. 3.5')
figure.add(prior, likelihood, posterior)
figure.show()
