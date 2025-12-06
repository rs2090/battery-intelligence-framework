"""
Dash app for the battery intelligence framework.
This app provides a web interface for uploading battery data, visualizing it, and running models.
"""

import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import dash_table
import networkx as nx
import io
from src.ingestion.data_loader import load_battery_data

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Battery Intelligence Framework"),
    dcc.Upload(
        id='upload-data',
        children=html.Div(['Drag and Drop or ', html.A('Select CSV File')]),
        style={
            'width': '50%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    html.Div(id='output-data-upload'),
])

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    import base64
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    return df

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'))
def update_output(contents, filename):
    if contents is not None:
        df = parse_contents(contents, filename)
        return html.Div([
            html.H5(filename),
            dash_table.DataTable(
                data=df.head().to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns]
            )
        ])
    return None

if __name__ == '__main__':
    app.run_server(debug=True)
