import sys
import os
import re

def get_file_paths(directory, filepath=[]):
    files = os.listdir(directory)
    for file in files:
        if not os.path.isfile(directory + '/' + file):
            get_file_paths(directory + '/' + file, filepath)
            continue
        filepath.append(directory + '/' + file)


# a = sys.argv[1]
def main():

    ip_addresses = []
    files = []
    directory = sys.argv[1]

    get_file_paths(directory, files)
    for file in files:
        with open(file, 'r') as f:
            # check for valid ip address
            ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', f.read())

            valid_ips = []
            for i, ip in enumerate(ips):
                is_valid = all(0 <= int(octet) <= 255 for octet in ip.split('.'))
                if is_valid:
                    valid_ips.append(ip)

            ip_addresses.extend(valid_ips)

    ip_addresses = list(set(ip_addresses))
    ip_addresses.sort()
    for ip in ip_addresses:
        print(ip)

if __name__ == "__main__":
    main()

