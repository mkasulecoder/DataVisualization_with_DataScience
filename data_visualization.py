import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
DATA Visualization Iin DATA Science for temperatures
at the Airpport of Helsinki-Vantaa Airport
@Mark Kasule
"""

# Save the file name
dataFileName = "./helsinki-vantaa.txt"
# Convert to dataframe, remove tabbed spaces, primary key/index = DATE
data = pd.read_csv(dataFileName, sep='\t', index_col='DATE')

# print the 5 rows of the data
print(data.head())

# Check number of rows in the data frame
print(len(data))  # alternative print(data) will show rows at end of table

"""
Part 2
"""
# Select data for the 30-year period (January 1988 to December 2018).
selection = data.loc['1/1/1988':'1/1/2018']
print(selection.head())

# Check the number of rows, enter output
print(f'Number of rows: {len(selection)}')

"""
Part 3
Create a line plot that displays the temperatures (TEMP_C) for each month in the 30-year time period with the following format:
•	Set the figure size
	Create a figure object and use the figsize parameter.
	The example figure uses figsize=(14,6) (you can experiment with other figure sizes if you like!)
•	Adjust the line style
	solid line
	black color
	round markers
•	Add a title and axis labels
	Title: 'Helsinki-Vantaa Airport'
	X-label: 'Time'
	Y-label: 'Temperature (Celsius)'
"""
# Get each year from date index
dates = selection.index  # all dates in the selection
years = list()  # all years in the selection

# Fetch each year
for each_year in dates:
    year = int(each_year.replace('1/1/', ''))  # remove dates and months from dates
    years.append(year)

# All years in the selection
# print(years)
# get each temp, convert it to list to remove unnecessary indices
temp_c = np.array(selection['TEMP_C'])
# print(temp_c)

# Create a plot
plt.figure(figsize=(20, 10))
plt.plot(years, temp_c, marker='o', color='black')

# Setting x-axis ticks to every 2 years
plt.xticks(years[::2])

# Add Labels. title
plt.title("'Helsinki-Vantaa Airport")
plt.xlabel("Time")
plt.ylabel("Temperature (Celsius)")

# Display plot
plt.grid(True)
plt.show()
