import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from ..data.loader import DataSchema

from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:

    all_month: list[str] = data[DataSchema.MONTH].tolist()
    unique_months = sorted(set(all_month))

    @app.callback(
        Output(component_id=ids.MONTH_DROPDOWN,
               component_property="value"),
        [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.SELECT_ALL_MONTHS_BUTTON, "n_clicks")],
    )
    def update_months(years: list[str], _: int) -> list[str]:
        return unique_months
        # filtered_data = data.query("year in @years")
        # return sorted(set(filtered_data[DataSchema.MONTH].tolist()))

    return html.Div(
        children=[
            html.H6("Month"),
            dcc.Dropdown(
                id=ids.MONTH_DROPDOWN,
                options=[{"label": month, "value": month}
                         for month in unique_months],
                value="unique_months",
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_MONTHS_BUTTON
            )
        ],
    )
