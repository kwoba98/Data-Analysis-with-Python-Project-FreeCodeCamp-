import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r"C:\AI programming with PYTHON\projects\Page View Time Series Visualizer\fcc-forum-pageviews.csv",
                 parse_dates=['date'], index_col='date')

# Clean data
# 1. Remove rows with NaN values
df = df.dropna()

# 2. Remove duplicate rows (if any)
df = df[~df.index.duplicated(keep='first')]





def draw_line_plot():
    # Create the figure and axis using subplots
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot the data using the DataFrame's index as the x-axis
    ax.plot(df.index, df['value'], color='skyblue', linewidth=1)

    # Add a title and axis labels
    ax.set_title("Daily Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save the figure
    fig.savefig('line_plot.png')

    # Return the figure object
    return fig



def draw_bar_plot():
    # 1. Make a copy of the DataFrame
    df_bar = df.copy()
    
    # 2. Extract year and month from the date index
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    # 3. Group by year and month, then calculate the average page views
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # 4. Order the months correctly
    months_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_grouped = df_grouped[months_order]
    
    # 5. Create the bar plot
    fig, ax = plt.subplots(figsize=(10, 8))
    df_grouped.plot(kind='bar', ax=ax)
    
    # 6. Customize the plot
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.set_title("Average Monthly Page Views per Year")
    ax.legend(title='Months', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # 7. Adjust layout to prevent clipping of labels
    plt.tight_layout()
    
    # 8. Save the figure
    fig.savefig('bar_plot.png')
    
    # 9. Return the figure object
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Ensure month order is correct for plotting
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise box plot
    sns.boxplot(x="year", y="value", data=df_box, ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(x="month", y="value", data=df_box, order=month_order, ax=ax2)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    # Adjust layout
    plt.tight_layout()

    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig
