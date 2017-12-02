import csv


def calculate_checksum(file_path):
    checksum = 0
    with open(file_path, 'r') as checksum_file:
        checksum_reader = csv.reader(checksum_file.readlines(), delimiter='\t')

        for row in checksum_reader:
            int_list = [int(i) for i in row]
            checksum += max(int_list) - min(int_list)
    return checksum


def calculate_evenly_divisible_checksum(file_path):
    checksum = 0
    with open(file_path, 'r') as checksum_file:
        checksum_reader = csv.reader(checksum_file.readlines(), delimiter='\t')

        for row in checksum_reader:
            int_list = [int(i) for i in row]

            for i in int_list:
                for j in int_list:
                    calc = float(i)/j
                    if calc.is_integer() and calc != 1:
                        checksum += calc
                        break

    return int(checksum)


