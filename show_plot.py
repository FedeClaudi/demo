from demo import Gaussian, Figure, teal, indigo_light


# create prior and likelihood distributoins
prior = Gaussian(
    mu=0, sigma=2.5, 
    label='prior:\n  $p_s(S_{hyp})$')

likelihood = Gaussian(
    mu=3.8, sigma=1, 
    color=teal, 
    label='likelihood:\n  $L(S_{hyp})=p_{x|s}(X_{obs}|S_{hyp})$',
    mu_label='$X_{obs}$')

# compute posterior
posterior = prior * likelihood
posterior.color = indigo_light  #  specify color
posterior.label = 'posterior:\n  $p_{s|x}(S_{hyp} | X_{obs})$'  # specify label
posterior.mu_label = '$\\hat{S}_{PM}$'

# create figure
figure = Figure(
    title='Fig. 3.5',
    xlabel='Hypothesized stimulus $S_{hyp}$',
    ylabel="Probability or likelihood",
)

# add gaussian distributions to plot
figure.add(prior, likelihood, posterior)

# show figure
figure.show()
