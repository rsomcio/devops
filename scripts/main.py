from collections import Counter, defaultdict


def main():
    with open('access.log', 'r') as f:
        data = f.readlines()

    parsed_data = [
            [tmp[0], tmp[3].split(':')[1], tmp[8]]
            for line in data
            if len(line.split()) >= 3
            for tmp in [line.split()]
            ]

    # top 5
    count_ips = Counter([i[0] for i in parsed_data])
    count_resp = Counter([i[2] for i in parsed_data])
    uniq_host_by_hour_map = defaultdict(set)

    for line in parsed_data:
        uniq_host_by_hour_map[line[1]].add(line[0]),
    print(f'hour\t unique ips\n{"-"*20}')

    for key, val in uniq_host_by_hour_map.items():
        print(f'{key}\t {len(val)}')
    print(f"success rate: {count_resp['200']/sum(count_resp.values())}")
    print(f"top 5: {count_ips.most_common(5)}")


if __name__ == "__main__":
    main()
