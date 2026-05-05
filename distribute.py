#binomal distribution => models the number of successes in a fixed number of independent trials
#probability of observing more than six(6) heads from ten(10) coin flips
import scipy.stats as stats

prob1=1-stats.binom.cdf(6,10,0.5)
print("The probability of observing more than six(6) heads in ten(10) fair coin flips is",prob1)

#poisson distribution => descries the number of times an event happens in a fixed interval
#conditions= constant rate(lambda), events are independent and can't happen at the same time
#expect rain ten(10) times in thirty(30) days
#probability of exactly six(6) days of rain

prob2=stats.poisson.pmf(6,10)
print("Probability of raining exactly six days is",prob2)

prob3=stats.poisson.pmf(12,10)+stats.poisson.pmf(13,10)+stats.poisson.pmf(14,10)
print("The probability of raining 12-14 days is",prob3)


#Working at a call center where the average number of calls between 9am and 10am is 15 calls(lambda) what is the probability of observing more than 20 calls
prob4=1-stats.poisson.cdf(20,15)
print("Probability of observing more than twenty calls is",prob4)

#observing between 17-21 calls
prob5=stats.poisson.cdf(21,15)-stats.poisson.cdf(16,15)
print("Probability of observing between 17-21 calls is",prob5)