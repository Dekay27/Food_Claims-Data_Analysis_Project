import pandas as pd

df = pd.read_csv('claims.csv')

print(df.head())

claim_id = df['claim_id']
time_to_close = df['time_to_close']
claim_amount = df['claim_amount']
amount_paid = df['amount_paid']
location = df['location']
individuals_on_claim = df['individuals_on_claim']
linked_cases = df['linked_cases']
cause = df['cause']

print('The unique values of claim_id are', claim_id.nunique())
print('The number of null values of claim_id are', claim_id.isnull().sum())

print('The unique values of time_to_close are', time_to_close.nunique())
print('The number of null values of time_to_close are', time_to_close.isnull().sum())

print('The unique values of claim_amount are', claim_amount.nunique())
print('The number of null values of claim_amount are', claim_amount.isnull().sum())

print('The unique values of amount_paid are', amount_paid.nunique())
print('The number of null values of amount_paid are', amount_paid.isnull().sum())

print('The unique values of location are', location.nunique())
print('The number of null values of location are', location.isnull().sum())

print('The unique values of individuals_on_claim are', individuals_on_claim.nunique())
print('The number of null values of individuals_on_claim are', individuals_on_claim.isnull().sum())

print('The unique values of linked_cases are', linked_cases.nunique())
print('The number of null values of linked_cases are', linked_cases.isnull().sum())

print('The unique values of cause are', cause.nunique())
print('The number of null values of cause are', cause.isnull().sum())

print(claim_amount.unique())
print("The existing type of claim_amount is", claim_amount.dtype)

# Removing the currency symbol from the entries
df['claim_amount'] = df['claim_amount'].apply(lambda x : x.split(' ')[-1])

# Updating claim_amount column to float64
df['claim_amount'] = df['claim_amount'].astype(float)

#Updating the figures to two decimal places
df['claim_amount'] = df['claim_amount'].round(2)

print("The updated type of claim_amount is", df['claim_amount'].dtype)

print('The number of null values in claim_amount is', df['claim_amount'].isna().sum())

# Calculate the median of non-null values in the 'amount_paid' column
median_value = df['claim_amount'].median(skipna=True)
print("The median value in claim_amount is", round(median_value, 2))

# Display the lowest and highest values in the amount_paid column
print("The lowest value in amount_paid is", df['amount_paid'].min())
print("The highest value in amount_paid is", df['amount_paid'].max())

# Calculate the median of non-null values in the 'amount_paid' column
median_value = df['amount_paid'].median(skipna=True)
print("The median value in amount_paid is", round(median_value, 2))

# Replace null values with the median value, rounded to two decimal places
df['amount_paid'].fillna(round(median_value, 2))

# Print the sum of null values in the updated DataFrame column
print("The number of null values in amount_paid is", df['amount_paid'].isnull().sum())

# Changing nan to FALSE
df['linked_cases'].fillna(False)
print("The number of null values in linked_cases is", df['linked_cases'].isnull().sum())
print("The unique values in linked_cases are", df['linked_cases'].unique())

# Update all entries to lowercase
df['cause'] = df['cause'].str.lower()

# Map incorrect entries to the correct ones. i.e., 'vegetables' with 'vegetable'
mapping = {
    'vegetables': 'vegetable',
    ' meat': 'meat'
}

df['cause'].replace(mapping)

# Replace any non-mapped entries with 'unknown'
df['cause'].fillna('unknown')

print("The unique values in cause are", df['cause'].unique())
print("The null values in cause are", df['cause'].isnull().sum())

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a custom pastel color palette
pastel_palette = ['#FFB6C1', '#FFDAB9', '#98FB98', '#DDA0DD']

# Create the visualization - Bar chart using Seaborn
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='location', palette=pastel_palette)
plt.xlabel('Location')
plt.ylabel('Number of Claims')
plt.title('Number of Claims in Each Location')

# Add annotations with the count values directly from the DataFrame
for idx, count in enumerate(df['location'].value_counts()):
    plt.text(idx, count, str(count), ha='center', va='bottom', color='grey', fontweight='bold')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

pastel_palette = ['#FFB6C1', '#98FB98', '#FFDAB9', '#DDA0DD']

# Get the count of claims in each location
location_counts = df['location'].value_counts()

# Create the visualization - Pie chart using Matplotlib with pastel palette
plt.figure(figsize=(8, 6))
plt.pie(location_counts, labels=location_counts.index, autopct='%1.1f%%',explode = [0.05,0.05,0.05,0.05], colors=pastel_palette)
plt.title('Proportion of Claims in Each Location')
plt.show()

# Chart visualization - Histogram using Seaborn
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='time_to_close', bins=10, kde=False, color='green')
plt.xlabel('Time to Close (days)')
plt.ylabel('Frequency')
plt.title('Distribution of Time to Close for All Claims (Histogram)')
plt.show()

# Chart visualization - KDE plot using Seaborn
plt.figure(figsize=(8, 6))
sns.kdeplot(data=df, x='time_to_close', color='green', fill=True)
plt.xlabel('Time to Close (days)')
plt.ylabel('Probability Density')
plt.title('Distribution of Time to Close for All Claims (KDE Plot)')
plt.show()


# Distribution metrics
# Calculate the skewness of the distribution
skewness = df['time_to_close'].skew()
print("Skewness:", skewness)

# Calculate the mean and median of the distribution
mean = df['time_to_close'].mean()
median = df['time_to_close'].median()

print("Mean:", mean)
print("Median:", median)

# Calculate the kurtosis of the distribution
kurtosis = df['time_to_close'].kurtosis()

print("Kurtosis:", kurtosis)

import numpy as np

# Add jitter to the time_to_close values for each location
jitter_amount = 0.3
df['jittered_time_to_close'] = df['time_to_close'] + np.random.uniform(-jitter_amount, jitter_amount, size=len(df))

# Chart visualization - Scatter plot with jitter using Seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='location', y='jittered_time_to_close', color='lightgreen', alpha=0.7)
plt.xlabel('Location')
plt.ylabel('Time to Close (days)')
plt.title('Time to Close vs. Location (Scatter Plot)')
plt.xticks(rotation=45)
plt.show()

# Chart visualization - Box plot using Seaborn
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='location', y='time_to_close', palette='pastel')
plt.xlabel('Location')
plt.ylabel('Time to Close (days)')
plt.title('Time to Close vs. Location')
plt.show()

# Group by 'location' and calculate the statistics for each group
grouped_stats = df.groupby('location')['time_to_close'].describe()

print(grouped_stats)