# main.py
from fasthtml import common as fh

app, rt = fh.fast_app(live=True)

@rt('/')
def get(): return fh.Div(fh.P('Live FastHTML Application!'))

fh.serve()