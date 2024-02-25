import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("projects/fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

# Clean data
df = df[(df['value'] >= df["value"].quantile(0.025)) & (df['value'] <= df["value"].quantile(0.975))]

def darw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(15,5))
    plt.plot(df.index, df["value"])
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Years"] = df_bar.index.year
    df_bar["Months"] = df_bar.index.month_name()

    df_bar = df_bar.groupby(["Years", "Months"], sort=False)["value"].agg(["mean"])
    df_bar = df_bar.reset_index()

    mis_data = {"Years":[2016,2016,2016, 2016],
            "Months":["January", "February","March","April"],
            "mean":[0,0,0,0]}
    df_bar = pd.concat([pd.DataFrame(mis_data), df_bar])  

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(9,6), dpi= 100)
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")
    ax.set_ylabel("Average Page Views")
    chart = sns.barplot(data=df_bar, x="Years", y="mean", hue="Months", palette="tab10")
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90, horizontalalignment='center')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    # df_box['year'] = [d.year for d in df_box.date]
    # df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # or
    df_box["Years"] = df_box.index.year
    df_box["Months"] = [x.month_name()[:3] for x in df_box.index]
    df_box.reset_index(inplace=True)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25,5))

    sns.boxplot(data = df_box, x= "Years", y="value", ax = axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")


    sns.boxplot(data= df_box, x="Months", y="value", order=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], ax= axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
