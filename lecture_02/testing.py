import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('train.csv')

# Replace all missing ages with the average age
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Grouping by 'Survived' and calculating the average age
avg_age_by_survival = df.groupby('Survived')['Age'].mean()

# Plotting the bar chart
avg_age_by_survival.plot(kind='bar', color=['red', 'green'])
plt.xlabel('Survived')
plt.ylabel('Average Age')
plt.title('Average Age of Passengers by Survival Status')
plt.xticks(ticks=[0, 1], labels=['Did Not Survive', 'Survived'], rotation=0)
plt.show()
