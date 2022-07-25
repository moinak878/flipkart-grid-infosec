import re
def ip_carve(filename):
    with open(filename) as fh:
        string = fh.readlines()

    valid =[]

    for line in string:
        line = line.rstrip()
        result = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
        valid +=result
    fh.close()
    return valid