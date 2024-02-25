import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import data
df = pd.read_csv('./projects/medical_data_visualizer/medical_examination.csv')

# Add 'overweight' column
df["overweight"] = (df["weight"] / np.square(df['height']/100) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1,
# make the value 0. If the value is more than 1, make the value 1.
df['gluc'] = (df['gluc'] > 1).astype(int)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 
    # 'active', and 'overweight'.
    l = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat = df.melt(id_vars=['cardio'], value_vars= np.sort(l)) # create a new df with varaible and value columns

    # Draw the catplot with 'sns.catplot()'
    graph = sns.catplot( data= df_cat, kind='count', x="variable", hue="value", col="cardio")

    # Get the figure for the output
    fig = graph.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
            (df['height']>= df['height'].quantile(0.025)) &
            (df['height'] <= df['height'].quantile(0.975)) &
            (df['weight']>= df['weight'].quantile(0.025)) & 
            (df['weight'] <= df['weight'].quantile(0.975))  ]
    
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(16, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig



