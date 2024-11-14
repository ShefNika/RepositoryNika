import collections
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as input_file:
        with open(OUTPUT_FILENAME, 'w') as output_file:
            reader = csv.DictReader(input_file, delimiter=',', quotechar='"')
            list_dict=[]
            for row in reader:
                list_dict.append(row)
            json.dump(list_dict, output_file, indent=4, ensure_ascii=True)






if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
