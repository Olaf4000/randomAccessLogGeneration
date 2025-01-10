import random
import string

def random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_host():
    random_host = random_host = 'www.' + str(random_string(4)) + '.pl'
    random_number = random.randint(1, 100)

    if random_number > 1 & random_number < 50:
        random_host = 'www.' + str(random_string(4)) + '.de'
        return random_host

    if random_number > 50 & random_number < 75:
        random_host = 'www.' + str(random_string(4)) + '.com'
        return random_host

    if random_number > 75 & random_number < 100:
        random_host = 'www.' + str(random_string(4)) + '.co.uk'
        return random_host

    return random_host

def generate_multiple_random_hosts(amount_of_hosts):
    random_hosts = []

    for i in range(amount_of_hosts):
        random_hosts.append(generate_random_host())

    return random_hosts
