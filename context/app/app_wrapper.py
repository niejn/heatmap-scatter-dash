import dash
from plotly.figure_factory.utils import PLOTLY_SCALES

from app.app_callbacks import configure_callbacks
from app.app_layout import configure_layout
from app.cluster import cluster
from app.pca import pca


class AppWrapper:

    def __init__(self, dataframe, cluster_rows=False, cluster_cols=False, colors='Greys'):
        self._dataframe = cluster(dataframe, cluster_rows=cluster_rows, cluster_cols=cluster_cols)
        self._dataframe_pca = pca(dataframe)
        self._conditions = self._dataframe.axes[1].tolist()
        self._color_scale = PLOTLY_SCALES[colors]
        self.app = dash.Dash()
        configure_layout(self)
        configure_callbacks(self)
