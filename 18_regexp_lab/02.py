import re


def toCamelCase(str):
    print re.sub(r'[\W_]', '', str)


print toCamelCase('adsa_da_dscsd_')
