import json

data: dict = json.load(open('logs.json', encoding='UTF-8'))

data = data[list(data.keys())[0]]

final_data = {}
for element in data:
    target_id = int(element["data"].split()[1])
    name = element["username"]
    if target_id != element["user_id"]:
        if final_data.get(name) is None:
            final_data[name] = 1
        else:
            final_data[name] += 1

f_data = []
for key, value in final_data.items():
    f_data.append((key, value))


f_data = sorted(f_data, key=lambda x: x[1])
total = 0
for entry in f_data:
    print(*entry)
    total += entry[1]

print(total)
