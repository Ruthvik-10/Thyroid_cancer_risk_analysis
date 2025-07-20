import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("thyroid_cancer_risk_data.csv")

Total_mean = df.groupby('Thyroid_Cancer_Risk')[['Age', 'TSH_Level', 'Nodule_Size']].mean()
print(Total_mean)

#box plot
melted_df = df.melt(id_vars='Thyroid_Cancer_Risk', value_vars=['Age', 'TSH_Level', 'Nodule_Size'])
plt.figure(figsize=(12, 6))
sns.boxplot(x='variable', y='value', hue='Thyroid_Cancer_Risk', data=melted_df)
plt.title('Boxplot of Age, TSH Level, and Nodule Size by Cancer Risk')
plt.ylabel('Values')
plt.xlabel('Parameters')
plt.legend(title='Cancer Risk')
plt.grid(True)
plt.show()

#scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='TSH_Level', y='Nodule_Size', hue='Thyroid_Cancer_Risk', style='Thyroid_Cancer_Risk', palette='Set2')
plt.title('Scatter Plot of TSH Level vs Nodule Size by Cancer Risk')
plt.xlabel('TSH Level (µIU/mL)')
plt.ylabel('Nodule Size (cm)')
plt.grid(True)
plt.legend(title='Cancer Risk')
plt.show()

