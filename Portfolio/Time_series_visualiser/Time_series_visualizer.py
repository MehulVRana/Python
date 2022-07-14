import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', drop = True, append = False, inplace = True, verify_integrity = False)

# Clean data by removing the outliers
df = df.loc[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    ''' 
        Creates a line plot 
      
        Args:

        Returns:
            fig : A line plot of the number of page views on any given day
    '''
    # Draw line plot
    # Initialise a figure 
    fig, ax = plt.subplots()
    plt.plot(df.index, df['value'], 'r')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig.set_size_inches(32,10)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    ''' 
        Creates a bar plot 
      
        Args:

        Returns:
            fig : A catplot of the average page views per month, grouped by 
            year.
    '''
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    # Create a column for the year and month data seperately
    df_bar['Months'] = df_bar.index.strftime('%B')
    df_bar['Years'] = df_bar.index.year
    month_ordered = ['January', 'February', 'March', 'April', 
            'May', 'June', 'July' , 'August' , 'September',
            'October', 'November', 'December']
    
    # Draw bar plot
    fig = sns.catplot(kind = 'bar', data = df_bar, x = 'Years', ci = None,
                      hue_order = month_ordered, hue = 'Months', y = 'value', 
                      legend = False)
    # Add figure text
    fig.set(ylabel = 'Average Page Views')
    plt.xticks(rotation = 90)
    plt.legend(loc = 'upper left', title = 'Months')
    fig = fig.fig
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    ''' 
        Creates two box plots
      
        Args:

        Returns:
            fig : Two bar charts. The left chart is the number of views vs the
            year. The right chart is the number of views vs the month.
    '''
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    # Create a column for the year and month data seperately
    df_box['Years'] = [d.year for d in df_box.date]
    df_box['Months'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    month_ordered = ['Jan', 'Feb', 'Mar', 'Apr', 
        'May', 'Jun', 'Jul' , 'Aug' , 'Sep',
        'Oct', 'Nov', 'Dec']
    # Initialise the plots
    fig, (ax1, ax2) = plt.subplots(1, 2)

    # Create plot 1
    sns.boxplot(data = df_box, x = 'Years', y = 'value', ax = ax1)
    # Add figure text
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set(ylabel = 'Page Views')
    ax1.set(xlabel = 'Year')
    
    # Create plot 2
    sns.boxplot(data = df_box, x = 'Months', order = month_ordered, y = 'value',  ax = ax2)
    # Add figure text
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set(ylabel = 'Page Views')
    ax2.set(xlabel = 'Month')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_line_plot()
draw_bar_plot()    
draw_box_plot()