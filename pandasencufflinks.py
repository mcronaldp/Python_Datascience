import pandas as pd
import cufflinks as cf
from IPython.display import display,HTML
cf.set_config_file(sharing='public',theme='ggplot',offline=True)

df_population = pd.read_csv('population_total.csv')
print(df_population)