""" This code tries to predict manually which will be the expected value of x
when using a random sample experiment by computing for all possible x 
and proving that as N number of random experiment increases (tends to infinity), the more accurate the prediction 
will be. """

""" To be improved: how can I make the margin of error (see line 40) 
to adapt proportionally as n increase.
This of interest, because for large n of binomial trials (>1000) code does 
not adjut the margin of error proportioanlly."""


import scipy.stats as stats
import numpy as np

n_size = int(input("Give the size of your binomial experiment (n): "))
p_sucess = float(input("Give the robability of success in binomial experiment (p):"))
lenght_experiment = int(input("Give the length of the experiment of random samples: "))


def func(n_size,p_sucess,lenght_experiment):
      # 0. Declaring parameters
      # 1. Manual outcome randomization
      pmfs = []
      pmfs_dict = {}

      for i in range(n_size+1):
            pmfs.append(stats.binom.pmf(i,n_size,p_sucess)) # To be used for max_pmf
            pmfs_dict[i] = stats.binom.pmf(i,n_size,p_sucess) # Dictionary with x (outcome) as key and their probability distribution as values
      
      max_pmf = np.max(pmfs) # Compute the expected value of the array of pmfs
      map_to_max_pmf = next((key for key,value in pmfs_dict.items() if value == max_pmf), None) # Map the highest PMF to its x (outcome)


      print("Your pmfs are the following: ", pmfs_dict)
      print("Your x with highest PMF is: ", map_to_max_pmf, "\n", "-"*60)

      # 2. "Automatic" outcome randomization

      z = np.random.binomial(n_size,p_sucess,lenght_experiment) # Create a random experiment for a binomial distribution with the same parameters

      mean_of_z = np.mean(z) # Compute for the expected value 

      if abs(map_to_max_pmf-mean_of_z) <= 0.5: # Allow for +-.5 margin of error
            return(f"Your estimator (θ) for the expected value of the random sample of rvs is very close to the truth value (^θ) as {mean_of_z} ≈ {map_to_max_pmf}, thus n is sufficient")
      else:
            return(f"Increase n, {mean_of_z} not close to {map_to_max_pmf} ")
      
      
print(func(n_size,p_sucess,lenght_experiment)) # If you want to fix values for testing, replace inputs functions by your values
