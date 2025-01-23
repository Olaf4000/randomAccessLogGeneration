import sys
from shutil import Error

import pandas as pd
import hashlib

# input / output names

input_file_name = 'logs_to_anonymise.json'
output_file_name = 'logs_anonymised.json'

# functions
def sha256_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

# import and normalize data
try:
    logs_raw = pd.read_json(input_file_name)
except Error as e:
    raise e

logs_cut = logs_raw[['timestamp', 'action', 'httpRequest', 'host']]

logs_normalized = pd.json_normalize(logs_cut['httpRequest'])
logs = pd.concat([logs_cut, logs_normalized], axis=1)
logs.drop(['httpRequest'], axis=1, inplace=True)

# anonymise clientIp
for row in logs.itertuples():
    logs.at[row.Index, 'clientIp'] = sha256_hash(row[4])

with open(output_file_name, "w") as file:
    file.write(logs.to_json(orient='records'))

file.close()
