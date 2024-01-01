from fastapi import FastAPI, HTTPException
from typing import Optional
from datetime import datetime, timezone, timedelta

app = FastAPI()

def read_access_logs(start_time: datetime, end_time: datetime):
    access_logs = []

    # Replace this with the actual path to your access log file
    log_file_path = "/path/to/access.log"

    with open(log_file_path, "r") as file:
        for line in file:
            log_entry = parse_log_entry(line)
            if log_entry and start_time <= log_entry["timestamp"] <= end_time:
                access_logs.append(log_entry)

    return access_logs

def parse_log_entry(log_line: str):
    # Replace this with your actual log parsing logic
    # Assuming log format: IP - - [timestamp] "method path HTTP/version" status response_size "referrer" "user_agent"
    try:
        parts = log_line.split()
        timestamp_str = parts[3] + " " + parts[4]
        timestamp = datetime.strptime(timestamp_str, "[%d/%b/%Y:%H:%M:%S %z]")
        return {
            "ip": parts[0],
            "timestamp": timestamp,
            "method": parts[5][1:],  # Remove leading double quote
            "path": parts[6],
            "status": int(parts[8]),
            "response_size": int(parts[9]),
            "referrer": parts[10][1:-1],  # Remove surrounding double quotes
            "user_agent": parts[11][1:-1]  # Remove surrounding double quotes
        }
    except IndexError:
        return None

@app.get("/access-logs/")
async def get_access_logs(start_time: datetime, end_time: datetime):
    access_logs = read_access_logs(start_time, end_time)
    return access_logs
