import plotly.graph_objects as go


# Define the nodes with different colors
nodes = [

    {'label': 'Starting college -> BSCS', 'color': 'black'},

    # CASE - College of Art, science and education
    {'label': 'CASE - College of Art, Science and Education = 47 transfers', 'color': 'purple'},


    {'label': 'CoB - College of Business = 5 transfers ', 'color': 'purple'},

    {'label': '2017-2021 = 47 transfers ', 'color': 'purple'},
    # {'label': '2018-2019 = 12 transfers ', 'color': 'blue'},
    # {'label': '2019-2020 = 5 transfers ', 'color': 'red'},
    # {'label': '2020-2021 = 7 transfers ', 'color': 'green'},

    # CoB - College of Business
    {'label': '2017-2021 = 5 transfers '},
    # {'label': '2018-2019 = 1 transfers '},
    # {'label': '2019-2020 = 4 transfers '},
    # {'label': '2020-2021 = 0 transfers'},


#    CoC - College of Communication
    {'label': 'CoC - College of Communication = 1 transfers', 'color': 'purple'},
    {'label': '2017-2021 = 1 transfers '},
    # {'label': '2018-2019 = 0 transfers '},
    # {'label': '2019-2020 = 0 transfers '},
    # {'label': '2020-2021 = 1 transfers'},

    # CEC - College of Engineering and Computing
    {'label': 'CEC - College of Engineering and Computing = 61 transfers', 'color': 'purple'},
    {'label': '2017-2021 = 61 transfers '},
    # {'label': '2018-2019 = 4 transfers '},
    # {'label': '2019-2020 = 26 transfers '},
    # {'label': '2020-2021 = 26 transfers'},

    # Green School of International
    {'label': 'Green School of International = 1 transfers', 'color': 'purple'},
    {'label': '2017-2021 = 1 transfers '},
    # {'label': '2018-2019 = 0 transfers '},
    # {'label': '2019-2020 = 0 transfers '},
    # {'label': '2020-2021 = 0 transfers'},

    # Nursing
    {'label': 'Nursing = 0 transfers', 'color': 'pink'},
    {'label': '2017-2021 = 0 transfers '},
    # {'label': '2018-2019 = 0 transfers '},
    # {'label': '2019-2020 = 0 transfers '},
    # {'label': '2020-2021 = 0 transfers'},

    # Stempel College of Public Policy
    {'label': 'Stempel College of Public Policy = 0', 'color': 'purple'},
    {'label': '2017-2021 = 0 transfers '},
    # {'label': '2018-2019 = 0 transfers '},
    # {'label': '2019-2020 = 0 transfers '},
    # {'label': '2020-2021 = 0 transfers'},
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
    {'source': 1, 'target': 0, 'value': 47, 'color': 'lightblue'},  # BACS -> CASE - College of Art, Science and Education
    {'source': 0, 'target': 3, 'value': 47, 'color': 'lightblue'},
    # {'source': 0, 'target': 4, 'value': 5, 'color': 'lightblue'},
    # {'source': 0, 'target': 5, 'value': 5, 'color': 'lightblue'},
    # {'source': 0, 'target': 6, 'value': 5, 'color': 'lightblue'},

     # CoB - College of Business
  
    {'source': 2, 'target': 0, 'value': 5, 'color': 'lightgreen'},
    {'source': 0, 'target': 4, 'value': 5, 'color': 'lightgreen'},
    # {'source': 0, 'target': 8, 'value': 5, 'color': 'lightgreen'},
    # {'source': 0, 'target': 9, 'value': 5, 'color': 'lightgreen'},
    # {'source': 0, 'target': 10, 'value': 5, 'color': 'lightgreen'},

    #    CoC - College of Communication
    {'source': 5, 'target': 0, 'value': 1, 'color': 'silver'},
    {'source': 0, 'target': 6, 'value': 1, 'color': 'silver'},
    # {'source': 0, 'target': 13, 'value': 5, 'color': 'silver'},
    # {'source': 0, 'target': 14, 'value': 5, 'color': 'silver'},
    # {'source': 0, 'target': 15, 'value': 5, 'color': 'silver'},

    # CEC - College of Engineering and Computing
    {'source': 7, 'target': 0, 'value': 61, 'color': 'mediumpurple'},
    {'source': 0, 'target': 8, 'value': 61, 'color': 'mediumpurple'},
    # {'source': 0, 'target': 18, 'value': 5, 'color': 'mediumpurple'},
    # {'source': 0, 'target': 19, 'value': 5, 'color': 'mediumpurple'},
    # {'source': 0, 'target': 20, 'value': 5, 'color': 'mediumpurple'},

     # Green School of International
    {'source': 9, 'target': 0, 'value': 1, 'color': 'tan'},
    {'source': 0, 'target': 10, 'value': 1, 'color': 'tan'},
    # {'source': 0, 'target': 23, 'value': 5, 'color': 'tan'},
    # {'source': 0, 'target': 24, 'value': 5, 'color': 'tan'},
    # {'source': 0, 'target': 25, 'value': 5, 'color': 'tan'},

    # Nursing
    {'source': 11, 'target': 0, 'value': 1, 'color': 'peachpuff'},
    {'source': 0, 'target': 12, 'value': 1, 'color': 'peachpuff'},
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
    text='The Total number of transfers to BSCS from the years of 2017 - 2021 = 115',
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