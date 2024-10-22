# main.py
from fasthtml.common import *

app, rt = fast_app(live=True)

contacts = [
    {"name": "Jane Doe", "email": "john.doe@example.com"},
    {"name": "John Doe", "email": "john.doe@example.com"},
    {"name": "Bob Smith", "email": "bob.smith@example.com"}
]

items = Ul(*[Li(o["name"]) for o in contacts])

@rt('/')
def get():
    return Titled("Contact Book", Div(
        Ul(*items),
        H2('Add a new contact'),
        Button("Click me", onclick="alert('Hello World')")
    )
    )
    
serve()