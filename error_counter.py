from pathlib import Path
dir=Path(__file__).parent
filepath=dir/'app.log'
errorcount=0
with open(filepath, 'r') as file:
    for line in file:
        if "ERROR" in line:
            errorcount=errorcount+1
            print(line.strip())
print(f"\nerror count={errorcount}")
