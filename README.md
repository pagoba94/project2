# Project 2 - Can money buy happiness? Does good weather make people happier? 


![image](https://user-images.githubusercontent.com/127286755/235512532-632b62e7-c57d-43eb-a0c2-2afd090680a3.png)

## Introduction
It has always been said that *"money does not bring happiness"* and that *"good weather brings good faces".*  In fact, here there are two different links to several articles on the same subject:
- On the one hand, an article from the UNIVERSITY of NEBRASKA-LINCOLN says: *"Being Rich Isn't Necessarily the Path to Happiness."* *"Doing Makes us Happier than Having."* [(https://psychology.unl.edu/can-money-buy-happiness)]

- On the other hand, an article from The Washington Post says: *"Can money buy happiness? Scientists say it can."* [(https://www.washingtonpost.com/business/2023/03/08/money-wealth-happiness-study/)]

To see who is right, we analyzed several dataframes on the Happiness Score by countries and comparing their happiness data with the average temperature of the country and its population, to see if there is any relation.
 
The happiness data is on the average of four dataframes with the results obtained in 2015, 2017, 2019 and 2021, with 158 rows and 12 columns. The average annual temperature data by country is from 2011, the most recent I have found, and for the population data we have used data from 2019, so that it would be an intermediate year compared to the Happiness Score data.

The Happiness Score is a national average of the responses to the main life evaluation question asked in the Gallup World Poll (GWP), which uses the Cantril Ladder. They ask respondents to think of a step with the most excellent conceivable life for them being a 10 and the most exceedingly bad conceivable life being a and to rate their claim current lives on that scale. It is explained by the following factors: GDP per capita, Healthy Life Expectancy, Social support, Freedom to make life choices, Generosity, Corruption Perception and Residual error.

## Results
figures/Happiness_GDP_population.png



## Files

- data: folder with four csv dataframes.
- figures: folder with four html files and four png files. Those are the charts that we created.
- jupyter notebooks: two jupyter notebook files with all the previous researching, cleaning and transforming.
- src: three pyhton files with downloading, cleaning and vizualization functions.
- README.md
- main.py: The main file, you need to execute the file using *pyhton main.py* and see the results of the analysis.


## Technologies

Jupyter notebook
Python
html

### Libraries used:

- import pandas as pd
- import re
- import seaborn as sns
- import matplotlib.pyplot as plt
- import plotly.graph_objects as go
- import plotly.offline as opy
- import plotly.express as px
- import plotly.io as pio
- from lxml import html
- import requests

Git clone and you can execute the code on your terminal using: pyhton main.py

## References: 

- Kaggle - World Happiness Report up to 2022
Editors: John Helliwell, Richard Layard, Jeffrey D. Sachs, and Jan Emmanuel De Neve, Co-Editors; Lara Aknin, Haifang Huang and Shun Wang, Associate Editors; and Sharon Paculor, Production Editor
Citation: Helliwell, John F., Richard Layard, Jeffrey Sachs, and Jan-Emmanuel De Neve, eds. 2020. World Happiness Report 2020. New York: Sustainable Development Solutions Network
- "Average yearly temperature (1961-2020, Celsius) - by country". lebanese-economy-forum.com. Lebanese Economy  Forum. 
- Population Data: The World Bank Documents & Report API