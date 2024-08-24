import csv
from rich.console import Console
from rich.table import Table
from datetime import datetime, timedelta

CAIES = []
console = Console()


def main(): 
    # Extract contents of file
    Extract()
    # Sort Contents, by order of dates
    console.print(display(sorted_caies()))
    # And Display the list of caies, in order
    
def Extract():
    global CAIES
    # Store it in a dictionary, containg a list of dictionarys, each of which contains a list
    with open("dates.txt") as dfile:
        contents = [list(map(lambda cont: cont.strip(), content)) for content in csv.reader(dfile) if content] # does not include any empty lists

    for number, paper in enumerate(contents):
        CAIES.append({
            "paper" : f"{paper[0]}-{paper[1]}",
            "date" : datetime.strptime(paper[2], "%d %b"),
            "session": paper[3]
        })
        if CAIES[number]["session"] == "PM":
            CAIES[number]["date"] += timedelta(seconds=10)
            # PM Papers should come AFTER AM papers
    return

def sorted_caies():
    return sorted(CAIES, key= lambda subject: subject["date"])
    

def display(paper_list):

    table = Table(title="Sorted Exams")
    
    for header, style in {"DATE":"cyan", "PAPER":"magenta", "SESSION":"green"}.items():
        table.add_column(header,justify="center", style=style)
    
    for paper in paper_list:
        table.add_row(paper["date"].strftime("%d, %B"), paper["paper"], paper["session"])

    return table

if __name__ == "__main__":
    main()