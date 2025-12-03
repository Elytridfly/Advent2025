import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'code.txt')

with open(file_path, 'r') as file:
    values = [line.strip() for line in file.readlines() if line.strip()]

pos = 50
c = 0

for value in values:
    if value[0] == 'R':
        pos = (pos + int(value[1:])) % 100
    elif value[0] == 'L':
        pos = (pos - int(value[1:])) % 100
    if pos == 0:
        c += 1
    

print(f"Total values loaded: {len(values)}")
print(f"Times position is 0: {c}")

