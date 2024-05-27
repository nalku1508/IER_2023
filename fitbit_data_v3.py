import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'IER_Fitbit_Data_2024.csv'

# Read the file
data = pd.read_csv(file_path, encoding='latin1')


# Function to plot the Vigorous MET minutes per week for a specific year
def plot_vigorous_met_for_year(data, year):
    data_year = data[data['year'] == year].copy()

    # Replace NA/NaN values with 0 for relevant columns of week 1
    data_year.loc[:, ['tijd_zwa1_uur', 'tijd_zwa1_min', 'dag_zwa1']] = data_year[
        ['tijd_zwa1_uur', 'tijd_zwa1_min', 'dag_zwa1']].fillna(0)
    # Calculate the "Vigorous MET minutes per week" for week 1
    data_year['Vigorous_MET_minutes_per_week_1'] = 8 * (
                (data_year['tijd_zwa1_uur'] * 60 + data_year['tijd_zwa1_min']) * data_year['dag_zwa1'])

    # Replace NA/NaN values with 0 for relevant columns of week 2
    data_year.loc[:, ['tijd_zwa2_uur', 'tijd_zwa2_min', 'dag_zwa2']] = data_year[
        ['tijd_zwa2_uur', 'tijd_zwa2_min', 'dag_zwa2']].fillna(0)
    # Calculate the "Vigorous MET minutes per week" for week 2
    data_year['Vigorous_MET_minutes_per_week_2'] = 8 * (
                (data_year['tijd_zwa2_uur'] * 60 + data_year['tijd_zwa2_min']) * data_year['dag_zwa2'])

    # Calculate the average Vigorous MET minutes per week
    data_year['Avg_Vigorous_MET_minutes_per_week'] = (data_year['Vigorous_MET_minutes_per_week_1'] + data_year[
        'Vigorous_MET_minutes_per_week_2']) / 2

    # Reset the index to use it as x-axis
    data_year = data_year.reset_index()

    # Plot the data entry index vs Vigorous MET minutes per week for both weeks
    plt.figure(figsize=(10, 6))
    plt.plot(data_year.index, data_year['Vigorous_MET_minutes_per_week_1'], marker='o', linestyle='-', color='blue',
             alpha=0.7, label='Week 1')
    plt.plot(data_year.index, data_year['Vigorous_MET_minutes_per_week_2'], marker='o', linestyle='-', color='red',
             alpha=0.7, label='Week 2')
    plt.title(f'Vigorous MET Minutes Per Week for {year}',fontsize=20)
    plt.xlabel('Data Entry Index',fontsize=18)
    plt.ylabel('Vigorous MET Minutes Per Week',fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend(fontsize=16)
    plt.grid(True)
    plt.show()

    # Plot the data entry index vs Average Vigorous MET minutes per week
    plt.figure(figsize=(10, 6))
    plt.plot(data_year.index, data_year['Avg_Vigorous_MET_minutes_per_week'], marker='o', linestyle='-', color='green',
             alpha=0.7)
    plt.title(f'Average Vigorous MET Minutes Per Week for {year}',fontsize=20)
    plt.xlabel('Data Entry Index',fontsize=18)
    plt.ylabel('Average Vigorous MET Minutes Per Week',fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)
    plt.show()

    # Return the average data for further use
    return data_year['Avg_Vigorous_MET_minutes_per_week'].mean()


# List of years to process
years = [2019, 2020, 2021, 2022, 2023]

# Dictionary to store the average MET minutes for each year
avg_vigorous_met_per_year = {}

# Generate plots for each year and store the averages
for year in years:
    avg_vigorous_met_per_year[year] = plot_vigorous_met_for_year(data, year)

# Plot the average Vigorous MET minutes per week for all years in one plot
plt.figure(figsize=(10, 6))
plt.plot(list(avg_vigorous_met_per_year.keys()), list(avg_vigorous_met_per_year.values()), marker='o', linestyle='-',
         color='purple', alpha=0.7)
plt.title('Average Vigorous MET Minutes Per Week Comparison',fontsize=20)
plt.xlabel('Year',fontsize=18)
plt.ylabel('Average Vigorous MET Minutes Per Week',fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.grid(True)
plt.show()
