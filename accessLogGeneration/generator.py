#imports
import csv
import random
import pandas as pd
import numpy as np
import ip_generation as ipgen
import host_generation as hostgen

# input variables
min_amount = 100
max_amount = 1000
average_amount = 500
distribution = 0 #TODO:may delete
amount_of_anomaly = 4
amount_of_client = 500
amount_of_hoste = 5
timestamp_min = 100000
timestamp_max = 700000

# generation
with open("logs.csv", mode="w") as file:
    file.write('timestamp, action, host, clientIp, country, uri' + '\n')

    for i in range(amount_of_hoste):
        host = str(hostgen.generate_random_host())

        for j in range(amount_of_client):
            client_ip = str(ipgen.generate_random_ip())
            amount_of_requests = int(random.uniform(min_amount, max_amount))

            for k in range(amount_of_requests):
                timestamp = int(random.uniform(timestamp_min, timestamp_max))
                file.write(
                    str(timestamp) + ',' +
                    'ALLOW' + ',' +
                    str(host) + ',' +
                    str(client_ip) + ',' +
                    'DE' + ',' +
                    '/placeholder' + '\n'
                )
