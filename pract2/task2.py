import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import statsmodels.api as sm
from scipy import stats

ticker = 'GOOG'
option_data = yf.download(ticker, start='2024-07-01', end='2024-09-20')
option_data['Price_Change'] = option_data['Open'].diff() 

option_data.dropna(inplace=True)

x = np.arange(len(option_data)) 
y = option_data['Price_Change'].values

degree = 2 
poly_coeffs = np.polyfit(x, y, degree)

poly_func = np.poly1d(poly_coeffs)

y_pred = poly_func(x)


plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Суточное изменение цен', color='blue')
plt.plot(x, y_pred, label='Полиномиальное приближение', color='red')
plt.title('Полиномиальное приближение суточного изменения цен')
plt.xlabel('Дни')
plt.ylabel('Изменение цен')
plt.legend()
plt.grid()
plt.show()

X = sm.add_constant(x)  
model = sm.OLS(y, X).fit()
print(model.summary())

p_value = model.pvalues[1] 
print(f'p-значение: {p_value}')

alpha = 0.05
power = 1 - stats.norm.cdf(stats.norm.ppf(1 - alpha) - model.bse[1]/model.bse[0])
print(f'Мощность теста: {power}')