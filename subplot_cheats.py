# The faceting folly
import plotly.express as px
import pandas as pd

df = pd.read_pickle("my_xp_results.pkl")

# 1. using faceting to create subplots
fig = px.box(df, x='algorithm', y='final_rec_error', 
    facet_col="rank_est",
    facet_col_spacing=0.1, # in [0,1/(cols-1)] lol
    facet_col_wrap= 3, # how many subplots before next line
    facet_row="rank_est",
    facet_row_spacing=1 # in [0,1/(rows-1)] lol again
    )
# note: subplot index from left to right and bot to top
# 3 4
# 1 2


# 2. Using ??