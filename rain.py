import scipy.stats as stats

prob1=1-stats.poisson.cdf(12,10)
print("Probability of observing more than twelve days of rain is",prob1)

prob2=stats.poisson.cdf(18,10)-stats.poisson.cdf(11,10)
print("Probability of observing between 12-18 days of rain is",prob2)