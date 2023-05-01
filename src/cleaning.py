import pandas as pd
import re
import requests
from lxml import html


def cleaning_df2015(df, df2):
    """This function cleans and merges two dataframes based on a dictionary of country names and specific cleaning operations. 
    Args:
        :df: A pandas DataFrame with columns "Country", "Economy (GDP per Capita)",  and other columns that are not needed in 
        the final result.
        :df2: A pandas DataFrame with columns "Country", "Average yearly temperature (1961–1990 Celsius)".

    Returns:
        df: A merged DataFrame with the cleaned and renamed columns of both input dataframes.
    """
    
    countries_dict={'Denmark':'Denmark',
                    'Cyprus': 'Cyprus',
                    'Norway': 'Norway',
                    'Somalia': 'Somalia|Somaliland',
                    'Macedonia':'Macedonia',
                    'Swaziland': 'Eswatini',
                    'Democratic Republic of the Congo': 'Kinshasa', 
                    'Republic of the Congo':'Brazzaville'             
    }
    
    # Iterate over each element of the species2 column of the dataframe and replace the values for the keys
    for key, value in countries_dict.items():
        mask= df2['Country'].str.contains(value, case=False)
        df2.loc[mask, 'Country'] = key
    
    df2['Average yearly temperature (1961–1990 Celsius)'] = df2['Average yearly temperature (1961–1990 Celsius)'].str.replace('−', '-').astype(float)
    
    mask_Democratic = df['Country'].str.contains('Kinshasa', case=False)
    df.loc[mask_Democratic, 'Country'] = 'Democratic Republic of the Congo'
    
    mask_Congo = df['Country'].str.contains('Brazzaville', case=False)
    df.loc[mask_Congo, 'Country'] = 'Republic of the Congo'    
    
    mask_Somalia = df['Country'].str.contains('Somaliland', case=False)
    df.loc[mask_Somalia, 'Country'] = 'Somalia'
    
    df = pd.merge(df, df2, on='Country', how='outer')
    df = df.add_suffix(' 2015')
    df.rename(columns = {"Economy (GDP per Capita) 2015":"GDP per Capita 2015" ,
                         "Average yearly temperature (1961–1990 Celsius) 2015": "Average yearly temperature", 
                         "Country 2015": "Country", "Region 2015": "Region"}, inplace=True)
    
    df.drop(columns=["Region", "Standard Error 2015", "Family 2015", "Health (Life Expectancy) 2015", "Freedom 2015", 
                     "Trust (Government Corruption) 2015", "Generosity 2015", "Dystopia Residual 2015"], axis=1, inplace=True)
    
    
    return df


def cleaning_df2017(df):
    """This function cleans and renames columns of a dataframe of the 2017 happiness report and replaces some country names.
    
    Args:
        :df: A pandas DataFrame with columns "Country", "Happiness.Rank", "Happiness.Score", "Economy..GDP.per.Capita." and 
        other columns that are not needed in the final result.

    Returns:
        :df: A cleaned and renamed DataFrame with the specified columns for the 2017 happiness report. """
    
    df = df.add_suffix(' 2017')
    df.rename(columns = {"Country 2017" : "Country", 
                             "Happiness.Rank 2017" :"Happiness Rank 2017", 
                             "Happiness.Score 2017" : "Happiness Score 2017", 
                             "Economy..GDP.per.Capita. 2017": "GDP per Capita 2017"}, inplace=True)
    
    df.drop(columns=["Whisker.high 2017", "Whisker.low 2017", "Family 2017", "Health..Life.Expectancy. 2017", "Freedom 2017", 
                         "Generosity 2017", "Trust..Government.Corruption. 2017", "Dystopia.Residual 2017"], axis=1, inplace=True)
    
    mask_Taiwan = df['Country'].str.contains('Taiwan', case=False)
    df.loc[mask_Taiwan, 'Country'] = 'Taiwan'

    mask_HongKong = df['Country'].str.contains('Hong Kong', case=False)
    df.loc[mask_HongKong, 'Country'] = 'Hong Kong'

    mask_Democratic = df['Country'].str.contains('Kinshasa', case=False)
    df.loc[mask_Democratic, 'Country'] = 'Democratic Republic of the Congo'

    mask_Congo = df['Country'].str.contains('Brazzaville', case=False)
    df.loc[mask_Congo, 'Country'] = 'Republic of the Congo'

    return df
    

def cleaning_df2019(df):
    """This function cleans and renames columns of a dataframe of the 2019 happiness report and replaces some country names.
    
    Args:
        :df: A pandas DataFrame with columns "Country or region", "Overall rank", "Score", "GDP per Capita" and 
        other columns that are not needed in the final result.

    Returns:
        :df: A cleaned and renamed DataFrame with the specified columns for the 2019 happiness report. """
    
    
    df = df.add_suffix(' 2019')
    df.rename(columns = {"Country or region 2019" : "Country", 
                             "Overall rank 2019":"Happiness Rank 2019", 
                             "Score 2019": "Happiness Score 2019", 
                             "GDP per capita 2019":"GDP per Capita 2019" }, inplace=True)
    
    df.drop(columns=["Social support 2019", "Freedom to make life choices 2019", "Generosity 2019", 
                         "Perceptions of corruption 2019","Healthy life expectancy 2019"], axis=1, inplace=True)
    
    countries_dict={'Sudan':'Sudan',
                    'Cyprus': 'Cyprus',
                    'Somalia': 'Somalia|Somaliland',
                    'Macedonia':'Macedonia',
                    'Trinidad and Tobago': 'Trinidad & Tobago',
                    'Swaziland': 'Eswatini',
                    'Democratic Republic of the Congo': 'Kinshasa', 
                    'Republic of the Congo':'Brazzaville'     
    }
    
    # Iterate over each element of the species2 column of the dataframe and replace the values for the keys
    for key, value in countries_dict.items():
        mask= df['Country'].str.contains(value, case=False)
        df.loc[mask, 'Country'] = key
    
    return df


def cleaning_df2021(df):
    """This function cleans and renames columns of a dataframe of the 2021 happiness report and replaces some country names.
    It also creates a new column called "Happiness Rank 2021" with the rank of column "Ladder score".
    
    Args:
        :df: A pandas DataFrame with columns "ï»¿Country name", "Ladder score", "Explained by: Log GDP per capita 2021" and 
        other columns that are not needed in the final result.

    Returns:
        :df: A cleaned and renamed DataFrame with the specified columns for the 2021 happiness report. """
    
    df = df.add_suffix(' 2021')
    df.rename(columns = {"ï»¿Country name 2021" : "Country", 
                             "Ladder score 2021": "Happiness Score 2021", 
                             "Explained by: Log GDP per capita 2021":"GDP per Capita 2021"}, inplace=True)
    
    df.drop(columns=["Regional indicator 2021", "Standard error of ladder score 2021", "upperwhisker 2021", 
                         "lowerwhisker 2021","Social support 2021","Healthy life expectancy 2021", "Freedom to make life choices 2021", 
                         "Generosity 2021", "Perceptions of corruption 2021", "Ladder score in Dystopia 2021", 
                         "Explained by: Social support 2021", "Explained by: Healthy life expectancy 2021", 
                         "Explained by: Perceptions of corruption 2021", "Dystopia + residual 2021", "Explained by: Generosity 2021", 
                         "Explained by: Freedom to make life choices 2021","Logged GDP per capita 2021"  ], axis=1, inplace=True)
    
    mask_Taiwan = df['Country'].str.contains('Taiwan', case=False)
    df.loc[mask_Taiwan, 'Country'] = 'Taiwan'

    mask_Congo = df['Country'].str.contains('Brazzaville', case=False)
    df.loc[mask_Congo, 'Country'] = 'Republic of the Congo'

    mask_HongKong = df['Country'].str.contains('Hong Kong', case=False)
    df.loc[mask_HongKong, 'Country'] = 'Hong Kong'

    mask_Macedonia = df['Country'].str.contains('Macedonia', case=False)
    df.loc[mask_Macedonia, 'Country'] = 'Macedonia'
    
    df['Happiness Rank 2021'] = df['Happiness Score 2021'].rank(method='dense', ascending=False).astype(int)
    
    return df


def merging_df(df,df1,df2,df3):
    """This function merges four pandas DataFrames by country name.
    Args:
        :df: A pandas DataFrame with columns "Country" and other columns to be merged.
        :df1, df2, df3: Other pandas DataFrames with "Country" column and other columns to be merged.

    Returns:
        :df: A merged DataFrame with all the columns from the four input DataFrames, merged by country name. 
    
    """
    merged_df = pd.merge(df, df1, on='Country', how='outer')
    merged_df2 = pd.merge(merged_df, df2, on='Country', how='outer')
    merged_df3 = pd.merge(merged_df2, df3, on='Country', how='outer')
    df=merged_df3
    
    return df


def mean_columns(df):
    """ This functions addes a mean score of happiness and GDP per capita to a dataframe, eliminates rows with incomplete data 
    or irrelevant countries, and fills in missing values for temperature.

    Args:
        :df: a pandas Dataframe with happiness and GDP data

    Returns:
        :df: a pandas Dataframe with additional columns for mean happiness score and mean GDP per capita, as well as cleaned 
        and filled data."""
    
    df_score=df[['Country', 'Happiness Score 2015', 'Happiness Score 2017', 'Happiness Score 2019', 'Happiness Score 2021']]
    df_mean = df_score.loc[:, ['Happiness Score 2015', 'Happiness Score 2017', 'Happiness Score 2019', 'Happiness Score 2021']].mean(axis=1).round(2)
    df_score["Mean Score"]= df_mean
    df = df.dropna(subset=["Happiness Score 2015",
                       "Happiness Score 2017","Happiness Score 2019", 
                       "Happiness Score 2021"], how="all")
    
    eliminated_rows=['North Cyprus','Oman', 'Suriname', 'Belize', 'South Sudan', 'Maldives', 'Djibouti' ]
    for i in eliminated_rows:
        df = df.drop(df.loc[df['Country'] == i].index)
        
    df.loc[df['Country'] == 'Taiwan', 'Average yearly temperature'] = 27.0
    df.loc[df['Country'] == 'Kosovo', 'Average yearly temperature'] = 15.0
    df.loc[df['Country'] == 'Palestinian Territories', 'Average yearly temperature'] = 20
    
    df['Mean Happiness Score'] = df[['Happiness Score 2015', 'Happiness Score 2017', 'Happiness Score 2019', 
                                     'Happiness Score 2021']].mean(axis=1).round(3)
    
    df['Mean GDP per Capita'] = df[['GDP per Capita 2015', 'GDP per Capita 2017', 'GDP per Capita 2019', 
                                    'GDP per Capita 2021']].mean(axis=1).round(2)
    
    return df


def population_df(df):
    """ This function retrieves the population data for a given list of countries from the World Bank API and merge it with a 
    dataframe of happiness scores. The merged dataframe will be sorted by the mean happiness score in descending order, and a 
    column for mean rank will be added.

    Args:
        :df: A pandas Dataframe of happiness scores for a list of countries.

    Returns:
        :df: A merged dataframe of happiness scores and population data, sorted by mean happiness score in descending order.
    """
    
    import wbdata

    # Define the indicators we want to retrieve
    indicators = {"SP.POP.TOTL": "Population"}

    # Define the countries we want to retrieve data for
    countries = ['FI', 'DK', 'CH', 'IS', 'NO', 'NL', 'SE', 'NZ', 'CA', 'AU', 'IL', 'AT', 'CR', 'LU', 'IE', 'US', 'DE', 'GB', 
             'BE', 'CZ', 'AE', 'MX', 'FR', 'BR', 'MT', 'SG', 'CL', 'QA', 'TW', 'PA', 'UY', 'SA', 'ES', 'GT', 'AR', 'CO', 
             'BH', 'TH', 'TT', 'SK', 'IT', 'KW', 'SV', 'UZ', 'SI', 'PL', 'LT', 'NI', 'EC', 'JP', 'KZ', 'KR', 'CY', 'XK', 
             'BO', 'JM', 'RO', 'EE', 'PE', 'MD', 'MU', 'LV', 'RU', 'PY', 'MY', 'HR', 'BY', 'RS', 'LY', 'PH', 'PT', 'HU', 
             'HK', 'HN', 'TM', 'VE', 'DZ', 'ME', 'BA', 'KG', 'ID', 'TR', 'GR', 'DO', 'PK', 'VN', 'CN', 'AZ', 'MN', 'TJ', 
             'MK', 'BT', 'NG', 'MA', 'JO', 'SO', 'LB', 'NP', 'LA', 'AL', 'BG', 'ZA', 'CM', 'GM', 'GH', 'MZ', 'BD', 'PS', 
             'IR', 'TN', 'AM', 'IQ', 'CG', 'NA', 'SN', 'KE', 'CI', 'UA', 'GE', 'GA', 'SZ', 'ZM', 'CD', 'MM', 'NE', 'KH', 
             'ET', 'MR', 'SL', 'LK', 'EG', 'ML', 'BF', 'BJ', 'UG', 'LR', 'IN', 'GN', 'TD', 'KM', 'LS', 'AO', 'MG', 'SD', 
             'HT', 'MW', 'ZW', 'BW', 'YE', 'TG', 'TZ', 'RW', 'BI', 'SY', 'AF', 'CF'
    ]

    # Retrieve the data from the API and store it in a dataframe
    df2= wbdata.get_dataframe(indicators, country=countries)
    df2= df2.loc[df2.index.get_level_values("date") == "2019"]
    df2.reset_index(inplace=True)
    df2=df2.drop(columns=['date'])
    df2 = df2.rename(columns={'country': 'Country'})
    
    countries_dict={'Czech Republic':'Czechia',
                'Slovakia':'Slovak Republic',
                'South Korea':'Korea, Rep',
                'Russia':'Russian Federation',
                'Hong Kong':'Hong Kong SAR, China',
                'Venezuela':'Venezuela, RB',
                'Kyrgyzstan':'Kyrgyz Republic',
                'Turkey':'Turkiye',
                'Macedonia':'North Macedonia',
                'Laos':'Lao PDR',
                'Gambia':'Gambia, The',
                'Iran':'Iran, Islamic Rep.',
                'Republic of the Congo':'Congo, Rep.',
                'Ivory Coast':"Cote d'Ivoire" ,
                'Swaziland':'Eswatini',
                'Democratic Republic of the Congo': 'Congo, Dem. Rep.',
                'Egypt':'Egypt',
                'Yemen':'Yemen, Rep.',
                'Syria':'Syrian Arab Republic',
                'Palestinian Territories': 'West Bank and Gaza'
    }

    for key, value in countries_dict.items():
        mask= df2['Country'].str.contains(value, case=False)
        df2.loc[mask, 'Country'] = key
    
    merged_df = pd.merge(df, df2, on='Country', how='outer')
    merged_df.loc[merged_df['Country'] == 'Taiwan', 'Population'] = 23733876
    df=merged_df
    
    df['Mean Rank'] = df['Mean Happiness Score'].rank(method='dense', ascending=False).astype(int)
    
    df= df.sort_values("Mean Rank", ascending=True)
    df = df.reset_index(drop=True)
    
    return df