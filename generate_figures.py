# We are importing the pandas library, giving it a nickname 'pd', to help us read and handle our data table.
import pandas as pd

# We are importing the pyplot tool from the matplotlib library, nicknamed 'plt', which lets us draw charts.
import matplotlib.pyplot as plt

# We are importing the seaborn library, nicknamed 'sns', which makes our charts look beautiful automatically.
import seaborn as sns

# We are telling the pandas tool to read our CSV file (which is like a spreadsheet) and save it into a variable called 'data'.
data = pd.read_csv('heart_failure_clinical_records.csv')

# ==========================================
# Figure 1: Distribution (Histogram)
# ==========================================

# We are creating a new blank canvas (figure) for our first chart, making it 8 inches wide and 6 inches tall.
plt.figure(figsize=(8, 6))

# We are using seaborn to draw a histogram using the 'age' column from our 'data'.
# The 'hue' setting tells it to color the bars differently based on whether the patient passed away ('DEATH_EVENT').
sns.histplot(data=data, x='age', hue='DEATH_EVENT', multiple='stack')

# We are adding a title to the very top of our chart so people know what they are looking at.
plt.title('Figure 1: Distribution of Patient Age by Survival')

# We are saving our finished chart as an image file named 'figure_1_age_histogram.png' on the computer.
plt.savefig('figure_1_age_histogram.png')

# We are closing this chart canvas completely so our computer's memory doesn't get cluttered.
plt.close()

# ==========================================
# Figure 2: Boxplot
# ==========================================

# We are creating a new blank canvas for our second chart, also 8 by 6 inches.
plt.figure(figsize=(8, 6))

# We are using seaborn to draw a boxplot from our 'data'.
# The 'x' axis is the survival status ('DEATH_EVENT'), and the 'y' axis is the heart's pumping strength ('ejection_fraction').
sns.boxplot(data=data, x='DEATH_EVENT', y='ejection_fraction')

# We are adding a descriptive title to the top of our second chart.
plt.title('Figure 2: Ejection Fraction Boxplot by Survival')

# We are saving our second chart as an image file named 'figure_2_ejection_fraction_boxplot.png'.
plt.savefig('figure_2_ejection_fraction_boxplot.png')

# We are closing the second chart canvas to clean up.
plt.close()

# ==========================================
# Figure 3: Correlation (Scatterplot)
# ==========================================

# We are creating a new blank canvas for our third and final chart, 8 by 6 inches.
plt.figure(figsize=(8, 6))

# We are using seaborn to draw a scatterplot using our 'data'.
# The 'x' axis represents 'time' (follow-up days), and the 'y' axis is kidney health ('serum_creatinine').
# Again, the 'hue' setting colors the dots based on survival ('DEATH_EVENT').
sns.scatterplot(data=data, x='time', y='serum_creatinine', hue='DEATH_EVENT')

# We are giving our third chart a title explaining what it shows.
plt.title('Figure 3: Serum Creatinine vs. Time by Survival')

# We are saving our final chart as an image file named 'figure_3_creatinine_scatter.png'.
plt.savefig('figure_3_creatinine_scatter.png')

# We are closing the final chart canvas to finish tidying up!
plt.close()

# We are printing a friendly message to the screen so we know the program finished successfully.
print("All figures have been generated and saved successfully!")
