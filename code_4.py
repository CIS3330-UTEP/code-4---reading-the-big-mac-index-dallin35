import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    date_to_year = (df["date"].str[:4]).astype(int)
    iso_to_cc = df["iso_a3"].str.lower()
    df['year'] = date_to_year
    df['country_code'] = iso_to_cc
    year_df = df[(df['year'] == year)]
    mean = year_df.query('country_code == @country_code')['dollar_price'].mean()
    rounded_mean = round(mean,2)
    return rounded_mean

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    iso_to_cc = df["iso_a3"].str.lower()
    df['country_code'] = iso_to_cc
    cc_df = df[(df['country_code'] == country_code)]
    mean = cc_df['dollar_price'].mean()
    rounded_mean = round(mean,2)
    return rounded_mean

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    date_to_year = df['date'].str[:4].astype(int)
    df['year'] = date_to_year
    year_df = df[(df['year'] == year)]
    cheapest = year_df['dollar_price'].min()
    
    for index, row in year_df.iterrows():
        if row['dollar_price'] == cheapest:
            return f'{year_df["name"][index]}({year_df["iso_a3"][index]}): ${round(year_df["dollar_price"][index],2)}'

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    date_to_year = df["date"].str[:4].astype(int)
    df["year"] = date_to_year
    year_df = df[(df['year'] == year)]
    expensive = year_df['dollar_price'].max()

    for index, row in year_df.iterrows():
        if row['dollar_price'] == expensive:
            return f'{year_df["name"][index]}({year_df["iso_a3"][index]}): ${round(year_df["dollar_price"][index],2)}'

if __name__ == "__main__":
    get_big_mac_price_by_year(2012,'arg')
    get_big_mac_price_by_country('arg')
    get_the_cheapest_big_mac_price_by_year(2012)
    get_the_most_expensive_big_mac_price_by_year(2012)