# main.py
from fasthtml.common import *

def render(contact):
    return Li(f"{contact.name} - {contact.email}",
              A("Delete", hx_delete=f"/{contact.id}", hx_swap="outerHTML",
                target_id=f"contact-{contact.id}"),
              id=f"contact-{contact.id}")

app, rt, contacts, Contact = fast_app(
    'contacts.db',
    live=True,
    render=render,
    id=int,
    name=str,
    email=str,
    pk='id'
)

def create_contacts():
    if len(contacts()) == 0:
        contacts.insert(dict(name="Jane Doe", email="jane.doe@example.com"))
        contacts.insert(dict(name="John Doe", email="john.doe@example.com"))
        contacts.insert(dict(name="Bob Smith", email="bob.smith@example.com")
    )


@rt('/')
def get():
    
    create_contacts()
    
    return Titled("Contact Book", Div(
        Ul(*contacts(), id="contacts_list"),
        
        H2('Add a new contact'),
        Form(
            reset_name_input(),
            reset_email_input(),
            Button("Add Contact", hx_post="/", target_id="contacts_list", hx_swap="beforeend"),
        )
    )
    )

def reset_name_input():
    return Input(id="name", placeholder="Name", hx_swap_oob="true")

def reset_email_input():
    return Input(id="email", placeholder="Email", hx_swap_oob="true")

@rt('/')
def post(contact: Contact):
    contacts.insert(contact)
    return contact, reset_name_input(), reset_email_input()

@rt('{/}')
def delete(id:int):
    contacts.delete(id)

serve()

serve()