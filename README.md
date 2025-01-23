# randomAccessLogGeneration

## Description

repo to generate randomised access logs and anonymise existing ones

## setup

run `pip install -r requirements.txt` to install dependencies

## how to use access log generator

- set parameters in `generator.py` file
- `python generator.py` generates a file containing random log entrys 

## how to use access log anonymization

the access log anonymization consists of two scripts which serve different purposes

### format_to_json_list.py

as the name suggests this script transforms a file with new line seperated JSONs an formats it to
a proper JSON list.

It takes a text file called `logs_to_anonymise` and outputs a file called `logs_to_anonymise.json`. This file
is required by the anonymization script.

### anonymize.py

this scripts cuts the file to the necessary features and anonymizes the clientIp addresses. It takes a file called
`logs_to_anonymise.json` as an input and outputs a file called `logs.json`.
