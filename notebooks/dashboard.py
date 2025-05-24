
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load cleaned data
df = pd.read_csv("data/train_cleaned_for_dashboard.csv")

# Initialize the Dash app
app = Dash(__name__)
app.title = "HR Analytics Dashboard"

# Layout
app.layout = html.Div([
    html.H1("HR Analytics Dashboard", style={'textAlign': 'center'}),

    dcc.Graph(
        figure=px.histogram(df, x='training_hours', nbins=30, title='Distribution of Training Hours')
    ),

    dcc.Graph(
        figure=px.box(df, x='target', y='training_hours', title='Training Hours vs Target')
    ),

    dcc.Graph(
        figure=px.histogram(df, x='education_level', color='target', barmode='group', title='Education Level by Target')
    ),

    dcc.Graph(
        figure=px.histogram(df, x='company_size', color='target', barmode='group', title='Company Size by Target')
    ),

    dcc.Graph(
        figure=px.histogram(df, x='experience', color='target', barmode='group', title='Experience vs Target')
    )
])

if __name__ == "__main__":
    app.run(debug=True)
