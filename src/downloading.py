import pandas as pd
import re
from lxml import html
import requests

def downloading_csv(path):
    """This function downloads from a raw link and saves the dataframe locally.
    args:
        :path: string.
    returns: 
        :df: pandas Dataframe
    """
    df=pd.read_csv(path, encoding='latin')
    return df


def downloading_html(path): 
    """ This function downloads the HTML content from a specified path, reads it into a pandas dataframe and returns the first table 
    in the HTML content.
    args:
        :path: string. the link
    returns: 
        :df: pandas Dataframe
    """
    
    headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    res = requests.get(path, headers=headers)
    table = pd.read_html(res.content, encoding = 'utf8')
    df = table[0]
    return df

