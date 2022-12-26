import pandas as pd
import cufflinks as cf
from IPython.display import display,HTML
cf.set_config_file(sharing='public',theme='ggplot',offline=True)

df_population = pd.read_csv('population_total.csv')
print(df_population)

# dropping null values
df_population = df_population.dropna()
# reshaping the dataframe
df_population = df_population.pivot(index='year', columns='country',
                                    values='population')
print(df_population)
# selecting 5 countries
df_population = df_population[['United States', 'India', 'China',
                               'Indonesia', 'Brazil']]
print(df_population)
df_population.iplot(kind='line',xTitle='Years', yTitle='Population',
                    title='Population (1955-2020)')
print(df_population)

#verder gaan met: https://towardsdatascience.com/the-easiest-way-to-make-beautiful-interactive-visualizations-with-pandas-cdf6d5e91757