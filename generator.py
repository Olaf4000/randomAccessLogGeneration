from access_log_generation import generate_access_logs

amount_of_ips = 10
amount_of_hosts = 5
amount_of_anomalies = 2
max_occurrence = 20

logs = generate_access_logs(
    amount_of_ips,
    amount_of_hosts,
    amount_of_anomalies,
    max_occurrence
)

with open('logs', 'w') as file:
    for log in logs:
        file.write(log + '\n')