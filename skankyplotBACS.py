import plotly.graph_objects as go


# Define the nodes with different colors
nodes = [
    # CASE - College of Art, science and education
    {'label': 'Starting college -> BACS', 'color': 'black'},

    {'label': 'CASE - College of Art, Science and Education = 63 transfers', 'color': 'purple'},
    {'label': 'CoB - College of Business = 19 transfers ', 'color': 'purple'},

    # CASE - College of Art, science and education
    {'label': '2017 - 2021 = 63 transfers ', 'color': 'purple'},
    # {'label': '2017-2018 = 16 transfers ', 'color': 'purple'},
    # {'label': '2018-2019 = 28 transfers ', 'color': 'blue'},
    # {'label': '2019-2020 = 10 transfers ', 'color': 'red'},
    # {'label': '2020-2021 = 9 transfers ', 'color': 'green'},

    # CoB - College of Business
    {'label': '2017-2021 = 19 transfers '},
    # {'label': '2018-2019 = 5 transfers '},
    # {'label': '2019-2020 = 4 transfers '},
    # {'label': '2020-2021 = 5 transfers'},


#    CoC - College of Communication = 5
    {'label': 'CoC - College of Communication = 39 transfers', 'color': 'purple'},
    {'label': '2017-2021 = 39 transfers '},
    # {'label': '2018-2019 = 2 transfers '},
    # {'label': '2019-2020 = 35 transfers '},
    # {'label': '2020-2021 = 1 transfers'},

    # CEC - College of Engineering and Computingb= 7
    {'label': 'CEC - College of Engineering and Computing = 27 transfers', 'color': 'purple'},
    {'label': '2017-2021 = 27 transfers '},
    # {'label': '2018-2019 = 5 transfers '},
    # {'label': '2019-2020 = 2 transfers '},
    # {'label': '2020-2021 = 18 transfers'},

    # Green School of International = 9 
    {'label': 'Green School of International = 3 transfers', 'color': 'purple'},
    {'label': '2017-2021 = 3 transfers '},
    # {'label': '2018-2019 = 1 transfers '},
    # {'label': '2019-2020 = 0 transfers '},
    # {'label': '2020-2021 = 1 transfers'},

    # Nursing = 11
    {'label': 'Nursing = 5 transfers', 'color': 'pink'},
    {'label': '2017-2021 = 5 transfers '},
    # {'label': '2018-2019 = 0 transfers '},
    # {'label': '2019-2020 = 3 transfers '},
    # {'label': '2020-2021 = 1 transfers'},

    # Stempel College of Public Policy = 13
    {'label': 'Stempel College of Public Policy = 1', 'color': 'purple'},
    {'label': '2017-2021 = 1 transfers '},
    # {'label': '2018-2019 = 0 transfers '},
    # {'label': '2019-2020 = 0 transfers '},
    # {'label': '2020-2021 = 1 transfers'},
#     {'label': '2017-2018', 'color': 'lightblue'},
#     {'label': '2018-2019', 'color': 'lightgreen'},
#     {'label': '2019-2020', 'color': 'lightyellow'},
#     {'label': '2020-2021', 'color': 'lightgray'},
#     {'label': '2021-2022', 'color': 'lightpink'},
#     {'label': '2022-2023', 'color': 'lightcyan'},
#    {'label': '16', 'color': 'lightcyan'}
    
]

# Define the links
links = [

    {'source': 1, 'target': 0, 'value': 63, 'color': 'lightblue'},  # BACS -> CASE - College of Art, Science and Education
    {'source': 0, 'target': 3, 'value': 63, 'color': 'lightblue'},
    # {'source': 0, 'target': 4, 'value': 5, 'color': 'lightblue'},
    # {'source': 0, 'target': 5, 'value': 5, 'color': 'lightblue'},
    # {'source': 0, 'target': 6, 'value': 5, 'color': 'lightblue'},

     # CoB - College of Business
  
    {'source': 2, 'target': 0, 'value': 19, 'color': 'lightgreen'},
    {'source': 0, 'target': 4, 'value': 19, 'color': 'lightgreen'},
    # {'source': 0, 'target': 8, 'value': 5, 'color': 'lightgreen'},
    # {'source': 0, 'target': 9, 'value': 5, 'color': 'lightgreen'},
    # {'source': 0, 'target': 10, 'value': 5, 'color': 'lightgreen'},

    #    CoC - College of Communication
    {'source': 5, 'target': 0, 'value': 39, 'color': 'silver'},
    {'source': 0, 'target': 6, 'value': 39, 'color': 'silver'},
    # {'source': 0, 'target': 13, 'value': 5, 'color': 'silver'},
    # {'source': 0, 'target': 14, 'value': 5, 'color': 'silver'},
    # {'source': 0, 'target': 15, 'value': 5, 'color': 'silver'},

    # CEC - College of Engineering and Computing
    {'source': 7, 'target': 0, 'value': 27, 'color': 'mediumpurple'},
    {'source': 0, 'target': 8, 'value': 27, 'color': 'mediumpurple'},
    # {'source': 0, 'target': 18, 'value': 5, 'color': 'mediumpurple'},
    # {'source': 0, 'target': 19, 'value': 5, 'color': 'mediumpurple'},
    # {'source': 0, 'target': 20, 'value': 5, 'color': 'mediumpurple'},

     # Green School of International
    {'source': 9, 'target': 0, 'value': 3, 'color': 'tan'},
    {'source': 0, 'target': 10, 'value': 3, 'color': 'tan'},
    # {'source': 0, 'target': 23, 'value': 5, 'color': 'tan'},
    # {'source': 0, 'target': 24, 'value': 5, 'color': 'tan'},
    # {'source': 0, 'target': 25, 'value': 5, 'color': 'tan'},

    # Nursing
    {'source': 11, 'target': 0, 'value': 5, 'color': 'peachpuff'},
    {'source': 0, 'target': 12, 'value': 5, 'color': 'peachpuff'},
    # {'source': 0, 'target': 28, 'value': 5, 'color': 'peachpuff'},
    # {'source': 0, 'target': 29, 'value': 5, 'color': 'peachpuff'},
    # {'source': 0, 'target': 30, 'value': 5, 'color': 'peachpuff'},

    # Stempel College of Public Policy
    {'source': 13, 'target': 0, 'value': 1, 'color': 'mistyrose'},
    {'source': 0, 'target': 14, 'value': 1, 'color': 'mistyrose'},
    # {'source': 0, 'target': 33, 'value': 5, 'color': 'mistyrose'},
    # {'source': 0, 'target': 34, 'value': 5, 'color': 'mistyrose'},
    # {'source': 0, 'target': 35, 'value': 5, 'color': 'mistyrose'},



]

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=1,
        line=dict(color='black', width=0.5),
        label=[node['label'] for node in nodes],
        color=[node.get('color', 'blue') for node in nodes]  # Assign colors to nodes
    ),
    link=dict(
        source=[link['source'] for link in links],
        target=[link['target'] for link in links],
        value=[link['value'] for link in links],
        color=[link.get('color', 'gray') for link in links]   # Assign colors to links
    )
)])

fig.add_annotation(
    x=0.5, y=-0.1,
    xref='paper', yref='paper',
    text='The Total number of transfers to BACS from the years of 2017 - 2021 = 157',
    showarrow=False,
    font=dict(size=14)
)

# Customize the layout
fig.update_layout(
    title_text='College Flow',
    font=dict(size=12, color='black'),
    plot_bgcolor='black',
    paper_bgcolor='white'
)

# Display the Sankey diagram
fig.show()