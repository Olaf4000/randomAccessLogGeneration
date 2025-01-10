import random

def generate_random_ip():
    ip_byts = []

    for i in range(1, 5):
        ip_byts.append(random.randint(2, 254))

    return str(ip_byts[0]) + '.' + str(ip_byts[1]) + '.' + str(ip_byts[2]) + '.' + str(ip_byts[3])

def generate_multiple_random_ips(amount_of_ips):
    ip_list = []

    for i in range(amount_of_ips):
        ip_list.append(generate_random_ip())

    return ip_list
