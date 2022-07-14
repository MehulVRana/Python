import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    ''' 
    Returns out the ledgertable in a pretty format
    
    Args:
        self (str): Defined by the intialisation.

    Returns:
        str : formatted ledgertable
    '''
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Drop unessacary columns
    df = df.drop(['Lower Error Bound', 'Upper Error Bound', 'NOAA Adjusted Sea Level'], axis = 1)
    # Change column type
    df['Year'] = df['Year'].astype(int)
    # Simplify colomn name
    df = df.rename(columns={'CSIRO Adjusted Sea Level':'Sea Level (inches)'})

    # Create scatter plot
    fig, ax = plt.subplots()
    fig = plt.scatter(x = df['Year'], y = df['Sea Level (inches)'])

    # Calculate first line of best fit using data from all years 
    results = linregress(x = df['Year'], y = df['Sea Level (inches)']) 
    
    # Restrict the data to only consider years from 2000 onwards
    df_2000 = df[df['Year']>1999]
    
    # Calculate second line of best fit using the restricted data
    results_2000 = linregress(x = df_2000['Year'], y = df_2000['Sea Level (inches)'])

    latest_year = (df['Year'].iloc[-1])+1
    # Adjust the year to get the row/ index number
    row_num = latest_year - df['Year'].iloc[0]
    new_years = []
    new_index = []
    
    while latest_year < 2051:
        new_years.append(latest_year)
        new_index.append(row_num)
        latest_year += 1
        row_num += 1

    df_part_2 = pd.DataFrame(data = {'Year':new_years}, index = new_index)
    df = pd.concat([df, df_part_2])
    df_2000 = pd.concat([df_2000, df_part_2])
    
    # Create data for first line of best fit using data from all years 
    df['best_fit'] = df['Year'] * results[0] + results[1]

   # Create data for second line of best fit using the restricted data
    df_2000['best_fit'] = df_2000['Year'] * results_2000[0] + results_2000[1]
    
    # Plot the data points as lines    
    ax.plot(df['Year'], df['best_fit'], color = 'g')
    ax.plot(df_2000['Year'], df_2000['best_fit'], color = 'r')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set(ylabel = 'Sea Level (inches)')
    ax.set(xlabel = 'Year')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()