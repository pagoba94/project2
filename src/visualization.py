import plotly.graph_objects as go
import plotly.offline as opy
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio


def happiness_temperature_scatter(df):
    """Creates a scatter plot using Plotly Express that shows the relationship between the mean happiness score and 
    the average yearly temperature for each country in the given dataframe.

    Args:
        :df: A pandas dataframe containing the data to be plotted. The dataframe has the columns named 'Mean Happiness Score', 
        'Average yearly temperature', and 'Country'.

    Returns:
        None. Displays the resulting plot in the output cell using Plotly.
    """
    
    fig = px.scatter(df, x="Mean Happiness Score", y="Average yearly temperature", 
                     color="Average yearly temperature", hover_name="Country", title="Countries happiness Score and their temperature")
    
    pio.write_html(fig, file='figures/happiness_temperature_scatter.html', auto_open=True)
    fig.show()


def happiness_temperature(df):
    """Creates a line plot using Plotly Express to visualize the relationship between the mean happiness score 
    and the average yearly temperature of different countries in the input DataFrame `df`.
    
    Args:
        :df: A pandas dataframe containing the following columns:
        - 'Country': the name of the country (str)
        - 'Mean Happiness Score': the mean happiness score of the country (float)
        - 'Average yearly temperature': the average yearly temperature of the country in Celsius (float)

    Return:
    None
        Displays the Plotly figure object containing the line plot of the mean happiness score and 
        the average yearly temperature of each country in the input DataFrame `df`. """ 

    fig = px.line(df, x="Mean Happiness Score", y="Average yearly temperature", hover_name="Country", color_discrete_sequence=['#00BFFF'])
    fig.update_layout(title='Countries happiness Score and their temperature', xaxis=dict(tickfont=dict(size=12)), yaxis=dict(tickfont=dict(size=12)))
    fig.update_traces(mode='markers+lines', marker=dict(size=8))
    
    pio.write_html(fig, file='figures/happiness_temperature_line.html', auto_open=True)
    fig.show()


def happiness_worldmap(df):
    """Creates a choropleth map using Plotly to visualize the happiness rank and GDP per capita of different countries 
    in the input DataFrame `df`.

    Args:
        :df: A pandas dataframe containing the following columns:
        - 'Country': the name of the country (str)
        - 'Mean Rank': the mean happiness rank of the country (float)
        - 'Mean GDP per Capita': the mean GDP per capita of the country in US dollars (float)

    Return
    """

    fig = go.Figure(go.Choropleth(
        locations = df['Country'],
        locationmode = "country names",
        z = df['Mean Rank'],
        text = df['Mean GDP per Capita'],
        colorscale = 'bluyl',
        autocolorscale = False,
        reversescale = False,
        marker_line_color = '#efefef',
        marker_line_width = 0.5,
        colorbar_title = 'Happiness Rank',       
        )
    )
    fig.update_layout(
        title_text = 'Happiness Rank and GDP per capita',
        showlegend = False,
        geo = dict(
            scope = 'world',
            resolution = 50,
            projection_type = 'miller',
            showcoastlines = True,
            showocean = True,
            showcountries = True,
            oceancolor = '#eaeaea',
            lakecolor = '#eaeaea',
            coastlinecolor = '#dadada'
        )
    )

    pio.write_html(fig, file='figures/happiness_worldmap.html', auto_open=True)
    fig.show()


def happiness_GDP(df):
    # Ordenar DataFrame según 'Mean GDP per Capita'
    df_sorted = df.sort_values(by='Mean GDP per Capita')

    # Crear gráfica con DataFrame ordenado
    fig = px.scatter(df_sorted, x='Mean Happiness Score', y='Mean GDP per Capita', size='Population', 
                 color='Average yearly temperature', hover_name='Country', log_x=True, size_max=60)

    fig.update_layout(title='Relation between Happiness, Population and GDP per Capita',
                  xaxis_title='Mean Happiness Score',
                  yaxis_title='Mean GDP per Capita',
                  legend_title='Country')
    
    pio.write_html(fig, file='figures/happiness_GDP_population.html', auto_open=True)
    fig.show()


