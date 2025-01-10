from dotenv import load_dotenv
import os

from access_log_generation import generate_access_logs

load_dotenv()

amount_of_ips = os.getenv("AMOUNT_OF_IPS")
amount_of_hosts = os.getenv("AMOUNT_OF_HOSTS")
amount_of_anomalies = os.getenv("AMOUNT_OF_ANOMALIES")
max_occurrence = os.getenv("MAX_OCCURRENCE")

logs = generate_access_logs(
    amount_of_ips,
    amount_of_hosts,
    amount_of_anomalies,
    max_occurrence
)

with open('logs', 'w') as file:
    for log in logs:
        file.write(log + '\n')