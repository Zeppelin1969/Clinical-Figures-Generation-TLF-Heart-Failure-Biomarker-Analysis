
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

data = pd.read_csv('heart_failure_clinical_records.csv')

plt.figure(figsize=(8, 6))

# We are using seaborn to draw a histogram using the 'age' column from our 'data'.
# The 'hue' setting tells it to color the bars differently based on whether the patient passed away ('DEATH_EVENT').
sns.histplot(data=data, x='age', hue='DEATH_EVENT', multiple='stack')

plt.title('Figure 1: Distribution of Patient Age by Survival')

plt.savefig('figure_1_age_histogram.png')

plt.close()

plt.figure(figsize=(8, 6))

sns.boxplot(data=data, x='DEATH_EVENT', y='ejection_fraction')

plt.title('Figure 2: Ejection Fraction Boxplot by Survival')

plt.savefig('figure_2_ejection_fraction_boxplot.png')

plt.close()

plt.figure(figsize=(8, 6))

sns.scatterplot(data=data, x='time', y='serum_creatinine', hue='DEATH_EVENT')

plt.title('Figure 3: Serum Creatinine vs. Time by Survival')

plt.savefig('figure_3_creatinine_scatter.png')

plt.close()

print("All figures have been generated and saved successfully!")
