# How to create a template in plotly, using the common options in the cheatsheet

import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import pandas as pd

# We start with an empty template
my_template = go.layout.Template()

# Templates are in fact similar to figures (graph object with data and layout, same as figures)
# We can update them similarly to figures, but we don't have update_layout available

my_template.layout= dict(
    # insert layout property here, including axes
    # Basically anything from common_options.py, with ****_foo for xaxes,
    title_text="test",
    xaxis_color="#ff0000",
    colorway=['#ff0000', '#00ff00', '#0000ff'] # this changes the default colors
)

# For annotations we need to change the default
my_template.layout.annotationdefaults=dict(
            text="Great Plot", # text does not go through 
            font_size=25, # but color and fontsize do
            font_color="crimson"
            ) 

# For traces we don't template (? to be continued)

# Finally we can combine themes using + :p
pio.templates["my_template"]=my_template
pio.templates.default = "plotly+my_template"

# How to store/load templates:
# Save them in a python file (e.g. my_template.py, this file with only the template)
# and import the file like "import my_template", which will run the code once, creating the template, 
# then run "pio.templates.default = "plotly+my_template""

# import the data
df = pd.read_pickle("my_xp_results.pkl")

# which algorithm is more accurate? What is the impact of rank value?
fig = px.box(df, x='algorithm', y='final_rec_error', 
            title="Which algorithm is more accurate? Does rank have an impact?",
            template=my_template, points="all", facet_col="rank_est",
            color="algorithm", log_y=True)

fig.show()