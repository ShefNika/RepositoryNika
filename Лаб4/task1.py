import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as file:
        data = json.load(file)
        return round(sum([s["score"]*s["weight"] for s in data]), 3)


print(task())
