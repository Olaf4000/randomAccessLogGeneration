from shutil import Error

import pandas as pd
import hashlib

from numpy.f2py.auxfuncs import throw_error


# functions
def sha256_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

# import and normalize data
try:
    logs_raw = pd.read_json('logs_to_anonymise.json')
except Error as e:
    raise e

logs_cut = logs_raw[['timestamp', 'action', 'httpRequest', 'host']]

logs_normalized = pd.json_normalize(logs_cut['httpRequest'])
logs = pd.concat([logs_cut, logs_normalized], axis=1)
logs.drop(['httpRequest'], axis=1, inplace=True)

# anonymise clientIp
for row in logs.itertuples():
    logs.at[row.Index, 'clientIp'] = sha256_hash(row[4])

with open("logs_anonymised.json", "w") as file:
    file.write(logs.to_json(orient='records'))

file.close()
