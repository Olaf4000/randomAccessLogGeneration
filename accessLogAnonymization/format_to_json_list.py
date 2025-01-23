# format to json list
log_files = open("logs_to_anonymise", "r", encoding="utf-8")

content = (
    '[' +
    log_files.read().replace('\n', ',') +
    ']'
)

# write result into file
with open("logs_to_anonymise.json", "w") as logs_to_anonymize:
    logs_to_anonymize.write(content)

# closing of files
log_files.close()
logs_to_anonymize.close()