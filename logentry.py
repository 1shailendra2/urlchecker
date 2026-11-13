class LogEntry:
    def __init__(self,timestamp,level,message):
        self.timestamp=timestamp
        self.level=level
        self.message=message
    def is_error(self):
        if self.level== "ERROR":
            return True
        else:
            return False
def parse_line(line):
    b=line.split()
    if len(b)<3 or b[2] not in ("ERROR","WARNING","INFO","DEBUG"):
        return None
    timestamp= " ".join(b[0:2])
    level=b[2]
    message= " ".join(b[3:])
    return LogEntry(timestamp, level, message)

