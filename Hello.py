from datetime import datetime
import os

log_dir = "/opt/test/"
log_file = os.path.join(log_dir, "app_$(date '+%Y%m%d_%H%M%S').log")

os.makedirs(log_dir, exist_ok=True)

with open(log_file, "a") as f:
    f.write(f"{datetime.now()} Application started\n")
    f.write(f"{datetime.now()} Sample log entry\n")

print("Log file created and updated")
