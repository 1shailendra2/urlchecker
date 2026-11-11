from pathlib import Path
dir=Path(__file__).parent
filepath=dir/'app.log'
count={}
with open(filepath, 'r') as file:
    for line in file:
        a=line.split()
        if len(a)>2 and a[2] in ("INFO", "WARNING","ERROR", "DEBUG"):
           level=a[2]
           current=count.get(level,0)
           count[level]=current+1 
with open(dir/'summary.txt', 'w') as file:
    for key , value in count.items():
        file.write(f"{key}:{value}\n")
