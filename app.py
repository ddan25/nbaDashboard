from dash import Dash
from dashboard import layout  # assuming __init__.py exposes layout

app = Dash(__name__)
app.layout = layout

if __name__ == '__main__':
    app.run(debug=True)
