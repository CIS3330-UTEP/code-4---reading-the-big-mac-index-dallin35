import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv('big-mac-full-index.csv')

# print(df.columns)
# Index(['date', 'iso_a3', 'currency_code', 'name', 'local_price', 'dollar_ex',
#        'dollar_price', 'USD_raw', 'EUR_raw', 'GBP_raw', 'JPY_raw', 'CNY_raw',
#        'GDP_bigmac', 'adj_price', 'USD_adjusted', 'EUR_adjusted',
#        'GBP_adjusted', 'JPY_adjusted', 'CNY_adjusted']

def get_big_mac_price_by_year(year,country_code):
    query = f"date >= '{year}-01-01' and date < '{year + 1}-01-01' and iso_a3 == '{country_code.upper()}'"
    q_df = df.query(query)
    return round(q_df["dollar_price"].mean(), 2)

def get_big_mac_price_by_country(country_code):
    query = f"iso_a3 == '{country_code.upper()}'"
    q_df = df.query(query)
    return round(q_df["dollar_price"].mean(), 2)

def get_the_cheapest_big_mac_price_by_year(year):
    query = f"date >= '{year}-01-01' and date < '{year + 1}-01-01'"
    q_df = df.query(query)
    min_row = q_df.loc[q_df["dollar_price"].idxmin()]
    return f"{min_row["name"]}({min_row["iso_a3"]}): {round(min_row["dollar_price"],2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    query = f"date >= '{year}-01-01' and date < '{year + 1}-01-01'"
    q_df = df.query(query)
    max_row = q_df.loc[q_df["dollar_price"].idxmax()]
    return f"{max_row["name"]}({max_row["iso_a3"]}): {round(max_row["dollar_price"],2)}"

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2012,'arg'))
    print(get_big_mac_price_by_country('arg'))
    print(get_the_cheapest_big_mac_price_by_year(2008))
    print(get_the_most_expensive_big_mac_price_by_year(2003))