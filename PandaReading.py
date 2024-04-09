import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import random
import seaborn as sns

df = pd.read_csv('table_data.csv') # read the csv data set
#print(df) #Our cute looking dataframe

# The first column originally doesn't have a name
df.columns.values[0] = 'Race'  # Let's change that by assining it a value
print(df)

#Creating a an empty Data Frame for our sample
selected_lap_times = {}

for race in df.index:
    # Select six random lap times
    selected_lap_times[race] = random.sample(df.loc[race, 'Lap 2':'Lap 7'].tolist(), 6) 
    #Recording lap times for laps 2 to 7
df_selected_lap_times = pd.DataFrame({'Lap Times': selected_lap_times}) #Creating a date frame for the times  
print(df_selected_lap_times)

#Join different arrays from the DataFrame into a single axis
#Numpy methods do not function with pandas DataFrames
lap_times_flat = np.concatenate(df_selected_lap_times['Lap Times'].values)


# Plot the histogram
plt.hist(lap_times_flat, bins=5, density=True, alpha=0.7, color='skyblue', edgecolor='black')

# Draw a smooth curve through the tops of the bars using kernel density estimation of Seaborn Library
sns.kdeplot(lap_times_flat, color='red', linewidth=2)

#Adding Labels and a Grid to the graph
plt.xlabel('Lap time')
plt.ylabel('Frequency')
plt.title('Distribution of Lap Times for All Races')
plt.grid(True)
plt.show()

# Calculate the mean lap time
mean_lap_time = np.mean(lap_times_flat)
st_dev = np.std(lap_times_flat)

print(f"Mean Lap Time: {mean_lap_time:.2f} seconds")
print(f'Standard Deviation: {st_dev:.2f}')

#From the graph we can observe that curve has a noticeable hump around the mean value 
#and a strong rise and drop-off, before and after the mean 
#X ~ N(129.47, 2.01)
#From the histogram and the curve on top, we can see the distribution curve 
#Which gives us an estimate of the distribution

#Calculating IQR
q1= np.percentile(lap_times_flat, 25) #Getting Q1 and Q3 using the percentile method from Numpy
q3 = np.percentile(lap_times_flat, 75)
IQR = q3 - q1 

print(f' The IQR goes from {q1} to {q3}.')
print(f'The IQR is: {IQR:.2f}')

#Calculating  the 15th and 85th percentile
p15 = np.percentile(lap_times_flat, 15)
p85 = np.percentile(lap_times_flat, 85)
print(f'The 15th percentile is {p15:.2f}\n The 85th percentile is {p85:.2f}')

#Median
median = np.median(lap_times_flat)
print(f'The median is: {median:.2f}')

#Calculating P(x>=130)
threshold = 130
#Counting the sum of times which are higher or equal to the threshold
wanted_outcomes = sum(1 for time in lap_times_flat if time >= threshold)
print(f'The number of outcomes where x>= 130: {wanted_outcomes} ')
#Calculating P(x>130) using the formula : ((number of uccernces >= threhsold)/total number of occurences)
empirical_probability = wanted_outcomes / len(lap_times_flat)
print(f'P(x>=130) = {empirical_probability:.2f}')
print(f'The 85th percentile tells us that 85% of data values fall below {p85:.2f}.')
print(f'This tells us that a value higher than {p85:.2f} is higher than 85% of the lap times.')
