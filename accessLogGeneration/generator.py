#imports
import csv
import random
import pandas as pd
import numpy as np
import ip_generation as ipgen
import host_generation as hostgen

# input variables
min_amount = 800
max_amount = 900
average_amount = 500
amount_of_anomaly = 4
amount_of_client = 500
amount_of_hoste = 5
timestamp_min = 100000
timestamp_max = 700000

# functions
def random_timestamp():
    return random.randint(timestamp_min, timestamp_max)

# generation
with open("logs.csv", mode="w") as file:
    file.write('timestamp,action,host,clientIp,country,uri' + '\n')

    for i in range(amount_of_hoste):
        host = str(hostgen.generate_random_host())

        #generate_noise
        for j in range(amount_of_client):
            client_ip = str(ipgen.generate_random_ip())
            amount_of_requests = int(random.uniform(min_amount, max_amount))

            for k in range(amount_of_requests):
                timestamp = random_timestamp()
                file.write(
                    str(timestamp) + ',' +
                    'ALLOW' + ',' +
                    str(host) + ',' +
                    str(client_ip) + ',' +
                    'DE' + ',' +
                    '/placeholder' + '\n'
                )

        #generate high request anomaly
        for j in range(amount_of_anomaly):
            client_ip = str(ipgen.generate_random_ip())
            amount_of_requests = int((random.uniform(min_amount, max_amount)) + max_amount)

            for k in range(amount_of_requests):
                timestamp = random_timestamp()
                file.write(
                    str(timestamp) + ',' +
                    'ALLOW' + ',' +
                    str(host) + ',' +
                    str(client_ip) + ',' +
                    'DE' + ',' +
                    '/placeholder' + '\n'
                )
