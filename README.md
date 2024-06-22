# Plotting temperatures for Helsinki-Vantaa Airport
In this assignment we will plot monthly mean temperatures from the Helsinki-Vantaa airport for the past 30 years.   Be sure to comment your code during all parts of this assignment.
The final output should look like this:  
Input data
File helsinki-vantaa.csv monthly average temperatures from Helsinki Vantaa airport. Column descriptions:
  •	DATE: YEAR-MONTH-DAY (the time stamp contains the first day of each month, but values in other columns are average values for the whole month!)
  •	USAF: Station number
  •	TEMP_F: Monthly mean temperature in Fahrenheit
  •	TEMP_C: Monthly mean temperature in Celsius
  •	REF_TEMP_C: Long term average in Celsius (for the period 1988-2018)
  •	DIFF_C: Difference between monthly mean and long-term average in Celsius
  Additional information
  •	Use exactly the same variable names and file names as in the instructions.
Assessment
Your assessment will be based on following criteria:
  •	Loading the data file and using the dates as the index
  •	Selecting the data for the 30-year period as described
  •	Creating a line plot of the data with the specified format
  •	Adding a title and axis labels to the plot
  •	Saving and submitting a copy of the plot as a PNG file 
  •	Including comments that explain what most lines in the code do
  •	Submitting all required files

## Part 1
Load the Helsinki temperature data from the file  helsinki-vantaa.txt.
  •	Read the data into a variable called data using pandas
  •	Parse the dates from the column 'DATE' and set the dates as the index in the DataFrame
2. Enter your code here:

3. Enter the output for a test print of the first five rows

Check the number of rows in the data frame
print(len(data))

## Part 2
Select data for the 30-year period (January 1988 to December 2018).
  •	Store the selection in a new variable selection
  •	Enter your code here:
Enter the output for a test print of the following

## Part 3
Part 3.1
Create a line plot that displays the temperatures (TEMP_C) for each month in the 30-year time period with the following format:
  ### Set the figure size
    - Create a figure object and use the figsize parameter.
    - The example figure uses figsize=(14,6) (you can experiment with other figure sizes if you like!)
    - Adjust the line style
    - solid line
    - black color
    - round markers
  ### Add a title and axis labels
    - Title: 'Helsinki-Vantaa Airport'
    - X-label: 'Time'
    - Y-label: 'Temperature (Celsius)'
## Part 3.2
Save your figure as PNG file called temp_line_plot.png.
Enter all code below for Part 3.1 below and cut and paste your png file on the following page.

Cut and paste your temp_line_plot.png below:
