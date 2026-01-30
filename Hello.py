import os
from datetime import datetime

# Directory where the log file will be created
log_dir = "/opt/test"

# Make sure the directory exists
os.makedirs(log_dir, exist_ok=True)

# Create a dynamic filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(log_dir, f"app_{timestamp}.log")

# Write some sample content to the log
with open(log_file, "w") as f:
    f.write(f"{datetime.now()} INFO Sample log created\n")

print(f"Log file created: {log_file}")
