import os
from datetime import datetime
import subprocess

# -----------------------------
# CONFIGURATION
# -----------------------------
# Directory where the log file will be created on Jenkins server
log_dir = "/opt/test"

# Splunk UF server details
UF_USER = "ec2-user"                       # Splunk UF username
UF_HOST = "13.204.233.48"    # Splunk UF hostname or IP
UF_DIR = "/opt/splunkforwarder/etc/sysem/local"        # Directory monitored by UF

# -----------------------------
# CREATE LOG FILE
# -----------------------------
# Ensure the directory exists
os.makedirs(log_dir, exist_ok=True)

# Dynamic filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(log_dir, f"app_{timestamp}.log")

# Write sample content
with open(log_file, "w") as f:
    f.write(f"{datetime.now()} INFO Sample log created on Jenkins\n")

print(f"Log file created: {log_file}")

# -----------------------------
# SCP LOG FILE TO SPLUNK UF
# -----------------------------
scp_command = ["scp", log_file, f"{UF_USER}@{UF_HOST}:{UF_DIR}/"]

try:
    print(f"Copying {log_file} to {UF_USER}@{UF_HOST}:{UF_DIR}/ ...")
    subprocess.run(scp_command, check=True)
    print("File successfully copied to Splunk UF server")
except subprocess.CalledProcessError:
    print("ERROR: Failed to copy file to Splunk UF server")
