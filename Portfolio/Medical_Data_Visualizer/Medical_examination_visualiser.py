# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 18:39:24 2022

@author: jindo
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight']/df['height'])>0.45
df['overweight'] = df['overweight'].apply(lambda x : 1 if x else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['cholesterol'] = df['cholesterol'].apply(lambda x : 0 if x <= 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x : 0 if x <= 1 else 1)



# Draw Categorical Plot
def draw_cat_plot():
    ''' 
        Creates a cat plot 
      
        Args:

        Returns:
            fig : A catplot of the count of the 'cholesterol', 'gluc', 'smoke',
            'alco', 'active', 'overweight' columns split by cardio.
    '''
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    titles = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    titles.sort()
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = titles, ignore_index = True)

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data = df_cat, kind = 'count',  x = 'variable', hue = 'value', col = 'cardio')
    fig.set(ylabel = 'total')
    fig = fig.fig
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    ''' 
        Creates a cat plot with a mask of the upper triangle
      
        Args: 

        Returns:
            fig : A heatmap showing the correlation of the cleaned variables 
    '''
    # Clean the data
    df_heat = df
    df_heat = df_heat.loc[(df_heat['ap_lo'] <= df_heat['ap_hi'])]
    df_heat = df_heat.loc[(df_heat['age'] >= 14500) & (df_heat['age'] <= 23500)]
    df_heat = df_heat.loc[(df_heat['gender'] < 3)]
    df_heat = df_heat.loc[(df_heat['height'] >= 150) & (df_heat['height'] <= 175)]
    df_heat = df_heat.loc[(df_heat['weight'] >= 50) & (df_heat['weight'] <= 100)]
    
    # Calculate the correlation matrix
    corr = df_heat.corr().round(1)
    corr = corr.astype(float)
    

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype = np.bool)
    mask[np.triu_indices_from(mask)] = True
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, vmax=1, vmin=-.1, center=0, cmap='vlag', mask=mask, fmt = '.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig



draw_heat_map()

draw_cat_plot()