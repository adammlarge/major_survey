import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

app = typer.Typer()

@app.command()
def survey():
    # Initialize counters for each category and major
    category_counters = {
        "Science": 0,
        "Hum": 0,
        "Sosc": 0,
    }
    major_counters = {
        "Bio": 0,
        "Chem": 0,
        "Phys": 0,
        "CS": 0,
        "Pre-law": 0,
        "Lang": 0,
        "Art": 0,
        "Music": 0,
        "Philosophy": 0,
        "Econ": 0,
        "Poly-Sci": 0,
        "Enviro": 0,
        "Psych": 0,
        "Socio": 0,
    }

    category_to_major = {
        'Science': ["Bio", "Chem", "Phys", "CS", 'Psych'],
        "Hum": ['Lang', 'Art', 'Music', 'Philosophy'],
        "Sosc": ['Pre-law', 'Econ', 'Poly-Sci', 'Socio']
    }

    console = Console()


    # Define the opening line
    opening_line = Text.from_markup(
        "[bold magenta]Welcome to the Academic Dialect Survey![/bold magenta]",
        justify="center"
    )

    # Create a panel to display the opening line
    panel = Panel(opening_line, expand=False, title="Survey Introduction")

    # Print the panel
    console.print(panel)

    typer.echo("\nLet's get started!\n")

    # Questions and corresponding options
    category_questions = [
        ("When you look over someone's work, what would you say you do?", {
            "1. Review": "Science",
            "2. Critique": "Hum",
            "3. Assess": "Sosc",
        }),
    ]

    major_questions = [
        ("What word would you use to refer to your parents?", {
            "1. Progenitors": "Bio",
            "2. Oppressors": "Socio",
            "3. Unsupportive Assholes": "Art",
            "4. Investors": "Econ"
        })
    ]

    # Run the survey for category
    for question, options in category_questions:
        typer.echo(f"\n{question}\n")
        for answer, category in options.items():
            typer.echo(answer)

        # Get user input
        answer = typer.prompt("Your answer (Enter the number): ")
        # Increment counter based on answer
        if answer.isdigit():
            answer_index = int(answer) - 1
            category_answer = list(options.keys())[answer_index]
            category = options[category_answer]
            category_counters[category] += 1

    # Run the survey for major
    for question, options in major_questions:
        typer.echo(f"\n{question}\n")
        for answer, major in options.items():
            typer.echo(answer)
        answer = typer.prompt("Your answer (Enter the number): ")
        if answer.isdigit():
            answer_index = int(answer) - 1
            major_answer = list(options.keys())[answer_index]
            major = options[major_answer]
            major_counters[major] += 1

    # Determine the most selected major
    max_major = max(major_counters, key=major_counters.get)

    console.rule("Top 5 Majors", style="bold magenta")

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Major")
    table.add_column("Count")

    topn = 0  # Counter for top N majors
    for major, count in sorted(major_counters.items(), key=lambda item: item[1], reverse=True):
        if topn < 5:
            if count >0:
                table.add_row(major, str(count))
            topn += 1

    console.print(table)

    console.print(f"You are probably a [bold cyan]{max_major}[/bold cyan] major! If not, you might need to reconsider. This test is infallible.")


if __name__ == "__main__":
    app()
