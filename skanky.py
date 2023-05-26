import plotly.graph_objects as go

# Define the sets of flows
sets = [
    {
        'nodes': [
            {'label': 'CASE - College of Art, science and education'},
            {'label': 'Starting College -> BACS'},
            {'label': '2017-2018'},
            {'label': '2018-2019'},
            {'label': '2019-2020'},
            {'label': '2020-2021'}
        ],
        'links': [
            {'source': 0, 'target': 1, 'value': 1},
            {'source': 1, 'target': 2, 'value': 1},
            {'source': 1, 'target': 3, 'value': 1},
            {'source': 1, 'target': 4, 'value': 1},
            {'source': 1, 'target': 5, 'value': 1}
        ]
    },
    {
        'nodes': [
            {'label': 'CASE - College of Art, science and education'},
            {'label': 'Starting College -> BA'},
            {'label': '2017-2018 = 16'},
            {'label': '2018-2019 = 17'},
            {'label': '2019-2020'},
            {'label': '2020-2021'}
        ],
        'links': [
            {'source': 0, 'target': 1, 'value': 1},
            {'source': 1, 'target': 2, 'value': 1},
            {'source': 1, 'target': 3, 'value': 1},
            {'source': 1, 'target': 4, 'value': 1},
            {'source': 1, 'target': 5, 'value': 1}
        ]
    }
    # Add more sets as needed...
]

# Create a Sankey diagram for each set
for set_data in sets:
    # Extract nodes and links for the current set
    nodes = set_data['nodes']
    links = set_data['links']

    # Create the Sankey diagram figure
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color='black', width=0.5),
            label=[node['label'] for node in nodes],
        ),
        link=dict(
            source=[link['source'] for link in links],
            target=[link['target'] for link in links],
            value=[link['value'] for link in links],
        )
    )])

    # Customize the layout of the diagram
    fig.update_layout(
        title='Flow Diagram',
        font=dict(size=12, color='black'),
        plot_bgcolor='white'
    )

    # Display the diagram
    fig.show()
