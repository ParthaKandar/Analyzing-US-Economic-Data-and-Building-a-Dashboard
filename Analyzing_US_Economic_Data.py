import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()

def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)
    
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

import pandas as pd
link =pd.read_csv(links['GDP'])
link.head()

import pandas as pd
unemp = pd.read_csv(links['unemployment'])
unemp.head()

unemp2 = unemp[unemp['unemployment']>=8.5]
unemp2.head()

x = unemp['date']
gdp_change =link['change-current']
unemployment =unemp['unemployment']
title = "Analyzing US Economic Data and Building a Dashboard"
file_name = "index.html"

make_dashboard(x= x, gdp_change= gdp_change, unemployment= unemployment, title= title, file_name= file_name)
