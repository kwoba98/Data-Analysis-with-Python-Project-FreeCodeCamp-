import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
# Convert height from cm to meters for BMI calculation
df['Height_meters'] = df['height'] / 100

# Calculate BMI
df['BMI'] = df['weight'] / (df['Height_meters'] ** 2)

# Determine if the person is overweight
df['overweight'] = (df['BMI'] > 25).astype(int)



# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
# Define a function to normalize the values
def normalize_value(value):
    if value == 1:
        return 0
    elif value > 1:
        return 1

# Apply the normalization function to the 'cholesterol' and 'gluc' columns
df['cholesterol'] = df['cholesterol'].apply(normalize_value)
df['gluc'] = df['gluc'].apply(normalize_value)



# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df[['cholesterol','gluc','smoke', 'alco', 'active','overweight','cardio']]

    df_cat= pd.melt(df_cat)
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby('cardio').sum().reset_index()

     #Group the data by 'cardio' and calculate counts for each feature
    df_counts = df_cat.groupby('cardio').sum().reset_index()

    # Rename one of the columns for the catplot to work correctly
    df_counts = df_counts.rename(columns={'cardio': 'is_cardio'})

    # Draw the catplot with 'sns.catplot()'

    # Get the figure for the output
    fig = sns.catplot(data=df_counts, kind="bar")
    plt.show()


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[df['ap_lo'] <= df['ap_hi']]
    df_heat=df[df['height'] >= df['height'].quantile(0.025)]
    df_heat=df[df['height'] <= df['height'].quantile(0.975)]
    df_heat=df[df['weight'] >= df['weight'].quantile(0.025)]
    df_heat=df[df['weight'] <= df['weight'].quantile(0.975)]
    

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
    fig, ax =  plt.subplots(figsize=(8, 6))

    # Draw the heatmap with 'sns.heatmap()'
    
    sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title('Correlation Matrix')
    plt.show()


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

df.head()
draw_cat_plot()
draw_heat_map()
