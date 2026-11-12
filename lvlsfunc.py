from pathlib import Path
import sys
def read_lines(filepath):
    with open(filepath, 'r') as file:
        lines=file.readlines()
        return lines
def count_levels(lines):
    count={}
    for a in lines:
        b=a.split()
        if len(b)>2 and b[2] in ("INFO","WARNING","ERROR","DEBUG"):
            level=b[2]
            current=count.get(level,0)
            count[level]=current+1
    return count
def write_summary(counts,path):
    with open(path, 'w') as file:
        for key, value in counts.items():
            file.write(f"{key}: {value}\n")
if __name__ == "__main__":
    if len(sys.argv) !=3:
        print("it should be like this python lvlsfunc.py logfile outputfile")
        sys.exit(1)
    filepath=sys.argv[1]
    try:
        counts=count_levels(read_lines(filepath))
        write_summary(counts, sys.argv[2])
    except FileNotFoundError:
        print(f"file not found: {filepath}")
        sys.exit(1)

