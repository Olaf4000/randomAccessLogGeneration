import random
import json

import ip_generation as ig
import host_generation as hg

last_time_stamp = 1736517645656

def generate_log_entry(client_ip, host, time_stamp):

    json_content = {
        "timestamp": time_stamp,
        "action": "ALLOW",
        "httpRequest": {
            "clientIp": client_ip,
            "country": "PH",
            "uri": "/placeholder"
        },
        "host": host
    }
    return json.dumps(json_content)

"""
generates multiple random access log entries
@:param amount_of_ips: amount of different ips generated
@:param amount_of_hosts: amount of different hosts generated 
@:param amount_of_anomalies: amount of ip addresses that display anomalies 
@:param max_occurrence: the maximum number of occurrences of a ip address
"""
#TODO: implement amount_of_anomalies functionality
def generate_access_logs(amount_of_ips, amount_of_hosts, amount_of_anomalies, max_occurrence):
    possible_ip_addresses = ig.generate_multiple_random_ips(amount_of_ips)
    possible_host = hg.generate_multiple_random_hosts(amount_of_hosts)

    ip_addresses = []

    for ip in possible_ip_addresses:
        amount = random.randint(1, max_occurrence)

        for i in range(amount):
            ip_addresses.append(ip)

    log_entrys = []

    for i in range(len(ip_addresses)):
        log_entrys.append(
            generate_log_entry(
                ip_addresses[i],
                random.choice(possible_host),
                random.randint(1000, 301000)
            )
        )

    random.shuffle(log_entrys)
    return log_entrys
