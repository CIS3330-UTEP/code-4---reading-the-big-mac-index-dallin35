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

    country_codes = ['arg','aus','bra','can','che','chl','chn',
                    'cze','dnk','euz','gbr','hkg','hun','idn',
                    'isr','jpn','kor','mex','mys','nzl','pol',
                    'rus','sgp','swe','tha','twn','usa','zaf',
                    'are','aze','bhr','col','cri','egy','gtm',
                    'hon','hrv','jor','kwt','lbn','lka','mda',
                    'nic','nor','omn','pak','per','phl','qat',
                    'rou','sau','tur','ury','ven','vnm']
    if country_code.lower() in country_codes: 
        query_data = df[(df['iso_a3'].str.lower() == country_code.lower()) 
                        & 
                        (df['date'].str.startswith(str(year)))]
    
        round_a = round(query_data['dollar_price'].mean(),2)

    return round_a

def get_big_mac_price_by_country(country_code):
    
    country_codes = ['arg','aus','bra','can','che','chl','chn',
                    'cze','dnk','euz','gbr','hkg','hun','idn',
                    'isr','jpn','kor','mex','mys','nzl','pol',
                    'rus','sgp','swe','tha','twn','usa','zaf',
                    'are','aze','bhr','col','cri','egy','gtm',
                    'hon','hrv','jor','kwt','lbn','lka','mda',
                    'nic','nor','omn','pak','per','phl','qat',
                    'rou','sau','tur','ury','ven','vnm']
    if country_code.lower() in country_codes: 
        query_data = df[(df['iso_a3'].str.lower() == country_code.lower())]
    
        round_b = round(query_data['dollar_price'].mean(),2)

    return round_b

def get_the_cheapest_big_mac_price_by_year(year):
    
    years = df[df['date'].str.startswith(str(year))]
    price_c = years['dollar_price'].min() 
    link = years.query('dollar_price == @price_c')

    name = link['name'].iloc[0]
    country_name = link['iso_a3'].iloc[0].upper() 

    return f"{name}({country_name}): ${price_c:.2f}" 

def get_the_most_expensive_big_mac_price_by_year(year):

    years = df[df['date'].str.startswith(str(year))]
    price_d = years['dollar_price'].max() 
    link = years.query('dollar_price == @price_d')

    name = link['name'].iloc[0]
    country_name = link['iso_a3'].iloc[0].upper() 

    return f"{name}({country_name}): ${price_d:.2f}" 

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2009,"mex")
    print(result_a)
    
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    
    result_d = get_the_most_expensive_big_mac_price_by_year(2003)
    print(result_d)