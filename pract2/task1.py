import numpy as np
from scipy.stats import norm


mu_0 = 4  
mu_1 = 3  
sigma = 0.5  
alpha = 0.05  
z_alpha = norm.ppf(1 - alpha / 2) 

n = (z_alpha * sigma / (mu_0 - mu_1)) ** 2
n = round(n)  

print(f"Необходимое количество часов работы плиточника: {int(n)}")

z_beta = (mu_1 - mu_0 + (sigma * z_alpha) / np.sqrt(n)) / (sigma / np.sqrt(n))

power = norm.cdf(z_beta)
print(f"Мощность теста: {power:.4f}")