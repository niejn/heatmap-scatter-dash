import dash
from plotly.figure_factory.utils import PLOTLY_SCALES

from app.utils.pca import pca


class AppBase:

    def __init__(self, dataframe,
                 diff_dataframes={},
                 colors='Greys',
                 heatmap_type='svg'):
        self._dataframe = dataframe
        self._dataframe_pca = pca(self._dataframe)
        self._diff_dataframes = diff_dataframes
        self._conditions = self._dataframe.axes[1].tolist()
        self._genes = self._dataframe.axes[0].tolist()
        self._color_scale = PLOTLY_SCALES[colors]
        self._heatmap_type = heatmap_type
        self._css_urls = [
            'https://maxcdn.bootstrapcdn.com/'
            'bootstrap/3.3.7/css/bootstrap.min.css'
        ]
        self.app = dash.Dash()
        self.app.title = 'Heatmap + Scatterplots'
        # Works, but not officially supported:
        # https://community.plot.ly/t/including-page-titles-favicon-etc-in-dash-app/4648
