import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    query = df[(df['iso_a3'].str.lower() == country_code) & (df['date'].str.startswith(str(year)))]
    rounda = round(query['dollar_price'].mean(),2)
    return rounda

def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    # print(type(df.loc[0]["date"]))
    # df["date"] = pd.todatetime(df["date"])
    
    print(get_big_mac_price_by_year(2010,"usa"))