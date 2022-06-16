import plotly.express as px
import pandas as pd

# if needed, import the data
df = pd.read_pickle("my_xp_results.pkl")

# which algorithm is more accurate? What is the impact of rank value?
fig = px.box(df, x='algorithm', y='final_rec_error', 
            title="Which algorithm is more accurate? Does rank have an impact?",
            template="plotly_white", points="all", facet_col="rank_est",
            color="algorithm", log_y=True)

# quick word: Plotly has a very confusing magic underscore syntax, so
# go.Layout(title=dict(font=dict(...))) is the same than 
# go.Layout(title_font=dict(...))

# The same goes for things below, anytime an underscore is used, 
# plotly actually understand updating a dictionary


# Updating layout (title, fonts, figsize, templates, backgrounds)
fig.update_layout(
    # Check doc on plotly, update_layout. Actually quite clear but long
    # Title things
    title_font_size=25, # font size
    title_text="C'est stylé", # title
    title_x=.1, # position [0,1]
    title_yanchor="bottom", #anchor position, ["top","middle","bottom","auto"]
    
    # Legend things
    showlegend=True,
    legend_bgcolor="#eeeeee", # RBG, all formats accepted, here Hex
    legend_bordercolor="#000000",
    legend_borderwidth=2, # a bit useless 
    legend_font_size=20, # fonts always have these 3 options
    legend_font_color="black",
    legend_font_family="Comic Sans", 
    legend_title_font_size=10,
    legend_title_text="Name of the Algorithm",
    legend_x=-0.5, # x position in [-2,3] normalized so that borders are [0,1]
    legend_y=0, # y position in [-2,3]
    
    # Sizes of figure
    width=800, # in px
    height=600,
    
    # Global font
    font_color="#555555",
    font_family="Courier New", # does not erase other specified fonts
    # A few common font families
    # Sans-serif fonts: Arial, Comic Sans MS, Trebuchet MS, and Verdana
    # Serif fonts: Georgia and Times New Roman
    # Monospace fonts: Andale Mono and Courier New
    font_size=12,
    
    # Backgrounds
    paper_bgcolor="#dddddd",
    plot_bgcolor="#abcdef",
    
    # Colors
    # 3 ways to specify the nodes values (diverging, sequential, sequential minus)
    # not shown below
    colorscale_diverging=[[0,"#051017"],[0.5,"#ffffff"],[1,"#000000"]],    
    colorway=["#ffffff","#1f77b4", "#000000"], # change default trace color values
    # what does this do exactly??
    
    # Template
    template="plotly_white",  #['ggplot2', 'seaborn', 'simple_white', 'plotly',
         #'plotly_white', 'plotly_dark', 'presentation', 'xgridoff',
         #'ygridoff', 'gridon', 'none']
    
)

# Axes
# for subplots: 1st subplot is xaxis,xaxis2... but xaxes is all subplots
fig.update_xaxes(    
    #documentation: update_xaxis
    
    # axis line property
    color="#ff0000", # changes all colors associated (lines, ticks, grids, text)
    linecolor="#aa0123", # only the line axis color
    linewidth=10,
    showline=True,
    type="category", # "-", "log","linear","category","date"
    
    # Ticks things and grids
    nticks=2, # number of ticks
    #range=[0,1], # range of the ticks
    # care for log, and category is mapped to ints (but does not show in this eg)
    # Also affects yrange??
    dtick=1, # distance between ticks, not so useful for category
    showspikes=True, # shows the small tick lines
    showticklabels=True,
    tickcolor="#000000",
    ticklen=5, # length of ticks in px
    tickfont_size=8, # size of text of ticks, other txt options same format
    # Changing the ticks text is a little bit of work
    # first change ticks type to array, then update text and place them correctly
    tickmode="array",
    tickvals=[0,1], # list with the positions of the ticks
    ticktext=["Aliens","Me"],
    
    # axes title
    title_font_size=13, # same story as other fonts specs
    title_text="", # always put name on axes !!
    
    # grid
    gridcolor="#ffffff",
    gridwidth=1, # activates the grid for boxplot
    showgrid=True, # overwrites above if False
    
    # Numbers of the top/on the right (for y axis)
    mirror=False, # True, "ticks", "all", "allticks", False 
    
    # misc
    visible=True,
    zeroline=False, # puts a line at 0
    zerolinewidth=0
)

# Traces updates. Here we have a box trace, options are different? for line traces
fig.update_traces(
    # documentation: update_traces
    
    # Selection
    #selector=3,
    selector=dict(name="hals"), # use to select the trace being updated
    # Default plotly express names: the name used for the legend, or numerics?
    # To select all traces: selector=dict()
    # To select all traces of a subplot: sounds like a bad idea
    
    # name of the trace, also changes the legend
    name="HaLs",
    #showlegend=True, # shows legend or not for a single trace.
    # will repeat legend if used for all subplots !!
    
    # Trace appearence
    opacity=0.5, # in [0,1], 1 is not actually 100%
    width=0.8, # in data coordinate; for boxplots only
    orientation="v", # v or h, boxplot only
    # Marker things
    marker_color="#000000", # also accepts color ranges for colormaps
    # weirdly affects the box as well
    marker_opacity=0.5, #only dots
    marker_size=8, # in px
    marker_symbol="bowtie", # large choice, check update trace doc
    # for line plots, check marker_colorbar
    
    # box things, also for line plots
    line_color="#ff0000", # color of boxes (bounding lines, also changes inside)
    fillcolor="#0000ff"
    # line_dash...
)

# annotations updates, mainly subplot titles. 
# In principle, any non-standard piece of text in the plot
fig.update_annotations(
    # documentation at update_annotations
    font_size=14,
    text="Best plot"
)
# To update annotations for each subplot, we can loop over annotations
# and manually edit (sigh...)
for i,ann in enumerate(fig.layout.annotations):
    ann.text="Plot_"+str(i) 
# to add an annotation,
# fig.add_annotation()

#print(fig)

#
fig.show()