from fasthtml.common import *

app = FastHTML()

def nav_bar():
    return Nav(
        Div(
            A('Home', href='/', cls="px-4"),
            A('About', href='/about', cls="px-4"),
            A('Contact', href='/contact', cls="px-4"),
            cls="flex"
        ),
        cls="bg-gray-800 text-white p-4"
    )

@app.get("/")
def home():
    return Title(), Main(
                nav_bar(),
                H1('Welcome to My Portfolio'),
                P('Hi, I am Daniel, a Developer and Mechanical Engineer.'),
                Section(
                    H2('Projects'),
                    P('Here are some of my projects:'),
                    Ul(
                        Li('Project 1 - Description'),
                        Li('Project 2 - Description'),
                        Li('Project 3 - Description')
                    )
                )
            )

@app.get("/about")
def about():
    return Title(), Main(
                nav_bar(),
                H1('About Me'),
                P('Hello! I am Daniel Ogbuigwe. I have a background in mechanical engineering and computer science.'),
                P('I am passionate about web development and enjoy building interactive web applications.'),
            )

@app.get("/contact")
def contact():
    return Title(), Main(
                nav_bar(),
                H1('Contact Me'),
                P('Feel free to reach out to me through the following methods:'),
                Ul(
                    Li('Email: ogbuigwed@gmail.com'),
                    Li('GitHub: github.com/ogbidaniel')
                ),
            )

if __name__ == "__main__":
    app.run()
