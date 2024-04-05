from dash import Dash, Output, Input
import dash_bootstrap_components as dbc

from paralympics_dash.figures import line_chart, bar_gender_faceted
from paralympics_dash.layout_elements import row_one, row_two, row_three, row_four

external_stylesheets = [dbc.themes.BOOTSTRAP]
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Layout variables are in layout_elements.py

app.layout = dbc.Container([
    row_one,
    row_two,
    row_three,
    row_four,
])


@app.callback(
    Output(component_id='line', component_property='figure'),
    Input(component_id='type-dropdown', component_property='value')
)
def update_line_chart(chart_type):
    figure = line_chart(chart_type)
    return figure


@app.callback(
    Output(component_id='bar', component_property='figure'),
    Input(component_id='checklist-input', component_property='value')
)
def update_line_chart(event_type):
    figure = bar_gender_faceted(event_type)
    return figure



if __name__ == '__main__':
    app.run(debug=True, port=8050)
    # Runs on port 8050 by default, this just shows the parameter to use to change to another port if needed
