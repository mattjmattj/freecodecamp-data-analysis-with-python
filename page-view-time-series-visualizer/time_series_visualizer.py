import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
                 parse_dates=['date'],
                 index_col='date')

# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[(df['value'] > df['value'].quantile(0.025))
        & (df['value'] < df['value'].quantile(0.975))]


# Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.
def draw_line_plot():
  # Draw line plot
  df_plot = df.copy()

  fig, ax = plt.subplots(figsize=(30, 10))
  ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
  ax.set_xlabel("Date")
  ax.set_ylabel("Page Views")

  sns.lineplot(data=df_plot, palette=['r'])

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


# Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()

  df_bar['year'] = df_bar.index.year
  df_bar['month'] = df_bar.index.month_name()
  df_bar = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()

  # Draw bar plot
  fig, ax = plt.subplots(figsize=(20, 20))
  
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  sns.barplot(data=df_bar, x="year", y="value", hue="month", hue_order=months)
  ax.set_xlabel("Years")
  ax.set_ylabel("Average Page Views")

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig


# Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly.
def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  # 2 axes
  fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(30, 10))

  # Year-wise Box Plot (Trend)
  sns.boxplot(data=df_box, x="year", y="value", ax=axes[0])
  axes[0].set_title("Year-wise Box Plot (Trend)")
  axes[0].set_xlabel("Year")
  axes[0].set_ylabel("Page Views")

  # Month-wise Box Plot (Seasonality)
  # "Make sure the month labels on bottom start at Jan"
  months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  sns.boxplot(data=df_box, x="month", y="value", order=months, ax=axes[1])
  axes[1].set_title("Month-wise Box Plot (Seasonality)")
  axes[1].set_xlabel("Month")
  axes[1].set_ylabel("Page Views")
  
  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
