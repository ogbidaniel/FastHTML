from fasthtml.common import *
import pandas as pd

app, rt = fast_app(hdrs=[Script(src='https://cdn.tailwindcss.com')])

# Load your data
df = pd.read_excel('sample_data.xlsx')

def create_table_from_df(df, limit=10):
    """Create an HTML table from the DataFrame with a specified row limit."""
    df = df.head(limit)
    
    rows = [Tr(
        *[Td(f"{val}") for val in row],
        cls="even:bg-purple/5"
    ) for _, row in df.iterrows()]

    headers = df.columns.tolist()
    head = Thead(*map(Th, headers), cls="bg-purple/10")

    return Table(head, *rows, cls="w-full text-sm text-gray-700 bg-white shadow-md rounded-lg", id="data-table")

def filter_dataframe(df, sector=None, year=None):
    """Apply filters to the DataFrame based on the user's input."""
    if sector:
        df = df[df['SECTOR'] == sector]
    if year:
        df = df[df['YEAR'] == year]
    return df

@app.get("/")
def home():
    """Render the home page with filters and a button to generate the table."""
    sectors = df['SECTOR'].unique().tolist()
    years = df['YEAR'].unique().tolist()

    return Title("Data Explorer"), Main(
        Div(
            H1("Welcome to the Data Explorer", klass="text-3xl font-bold pb-4"),
            P("Explore and analyze your data with ease.", klass="pb-4 text-gray-400"),

            # Dropdown to select sector
            Div(
                Select(
                    Option("All Sectors", value=""),
                    *[Option(sector, value=sector) for sector in sectors],
                    name="sector",
                    klass="mr-2"
                ),
                Select(
                    Option("All Years", value=""),
                    *[Option(year, value=year) for year in years],
                    name="year",
                ),
                klass="flex mb-4"
            ),

            Button("Generate Table", klass="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded",
                   hx_post="/generate-table", hx_target="#table-container", hx_swap="innerHTML"),
            Div(id="table-container"),
        ),
        klass="container mx-auto p-4"
    )

@app.post("/generate-table")
def generate_table(data: dict):
    """Generate a filtered table based on user input."""
    sector = data.get('sector')
    year = data.get('year')
    
    filtered_df = filter_dataframe(df, sector, year)
    return create_table_from_df(filtered_df, limit=10)

if __name__ == "__main__":
    serve()
