import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def draw_plot():
    # Read  data from file
    df =pd.read_csv("projects/epa-sea-level.csv")
    
    # Create scatter plot
    plt.scatter(x= df["Year"], y=df["CSIRO Adjusted Sea Level"])
    result = stats.linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    #print(f"result.slope:{result.slope}", f"result.intercept:{result.intercept}")

    # Create first line of best fit
    start_year = df['Year'].min()
    end_year = 2050
    my_range = list(range(start_year, end_year+1))
    best_fit_data = {"year": my_range,
                     "dependent_value": list(map(lambda x: (result.intercept + result.slope*x), my_range)) }
    plt.plot(best_fit_data["year"], best_fit_data["dependent_value"], "r")

    # Create second line of best fit
    start_year = 2000
    end_year = 2050
    df_new = df[df["Year"]>= start_year]
    result = stats.linregress(df_new["Year"], df_new["CSIRO Adjusted Sea Level"])

    my_range = list(range(start_year, end_year))
    best_fit_data = {"Year":my_range,
                     "y_value":list(map(lambda x:(result.intercept+ result.slope*x), my_range))}
    plt.plot(best_fit_data["Year"], best_fit_data["y_value"], "g")

                       
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    # plt.show()
    # print(f"plt.gca: {plt.gca().get_title()}")
    return plt.gca()


draw_plot()