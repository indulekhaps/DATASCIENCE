import pandas as pd

customer = pd.read_csv('customer_data.csv')
customer.head()
import matplotlib.pyplot as plt

point = customer.iloc[:,3:5].values
x = point[:,0]
y = point[:,1]
plt.scatter(x,y,s=50,alpha=0.7)
plt.xlabel('Annual income (k$)')
plt.ylabel('Spending Score')
plt.show()