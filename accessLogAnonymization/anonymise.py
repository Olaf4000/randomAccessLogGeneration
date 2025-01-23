import pandas as pd
import hashlib

# functions
def sha256_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

# import and normalize data
logs_raw = pd.read_json('logs_to_anonymise.json')
logs_cut = logs_raw[['timestamp', 'action', 'httpRequest', 'host']]

logs_normalized = pd.json_normalize(logs_cut['httpRequest'])
logs = pd.concat([logs_cut, logs_normalized], axis=1)
logs.drop(['httpRequest'], axis=1, inplace=True)

for row in logs.itertuples():
    logs.at[row.Index, 'clientIp'] = sha256_hash(row[4])

print(logs)

with open("logs_anonymised.json", "w") as file:
    file.write(logs.to_json(orient='records'))

file.close()
