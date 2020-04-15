import os
import sys
import base64


def install_facets():
    is_facets_avail = os.path.isdir("facets")
    if not is_facets_avail:
        get_ipython().system_raw('git clone https://github.com/PAIR-code/facets')
        get_ipython().system_raw('jupyter nbextension install facets/facets-dist')
        sys.path.append(os.path.abspath('facets/facets_overview/python/'))


# usage => overview({ 'frame name': pandas_dataframe, 'other frame name': other_dataframe })
class overview(object):
    def __init__(self, dfs):
        install_facets()
        from generic_feature_statistics_generator import GenericFeatureStatisticsGenerator
        gfsg = GenericFeatureStatisticsGenerator()
        self.height = 800
        self._proto = gfsg.ProtoFromDataFrames([{ 'name': name, 'table': table } for name, table in dfs.items()])

    def _repr_html_(self):
        protostr = base64.b64encode(self._proto.SerializeToString()).decode("utf-8")

        HTML_TEMPLATE = """<link rel="import" href="nbextensions/facets-dist/facets-jupyter.html" >
                <facets-overview id="elem" height="{height}"></facets-overview>
                <script>
                  document.querySelector("#elem").protoInput = "{protostr}";
                </script>"""
        html = HTML_TEMPLATE.format(protostr=protostr, height=self.height)
        return html


# usage => dive(pandas_dataframe)
class dive(object):
    def __init__(self, data):
        self._data = data
        self.height = 800
        install_facets()

    def _repr_html_(self):
        HTML_TEMPLATE = """<link rel="import" href="nbextensions/facets-dist/facets-jupyter.html" >
            <facets-dive id="elem" height="{height}"></facets-dive>
            <script>
              document.querySelector("#elem").data = {data};
            </script>"""
        html = HTML_TEMPLATE.format(data=self._data.to_json(orient='records'), height=self.height)
        return html