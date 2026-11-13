from logentry import parse_line
from pathlib import Path
folder=Path(__file__).parent
filepath=folder/'app.log'
with open(filepath, 'r') as file:
    for line in file:
        pv=parse_line(line)
        if pv is not None and pv.is_error():
            print(f"{pv.timestamp}, {pv.message}")
