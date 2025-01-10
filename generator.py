from access_log_generation import generate_access_logs

amount_of_ips = 100
amount_of_hosts = 10
amount_of_anomalies = 2
max_occurrence = 50

logs = generate_access_logs(
    amount_of_ips,
    amount_of_hosts,
    amount_of_anomalies,
    max_occurrence
)

with open('logs', 'w') as file:
    for log in logs:
        file.write(log + '\n')

with open("logs.json", "w") as file:
    file.write('[')

    for log in logs:
        file.write(log + ',')

    file.write(']')