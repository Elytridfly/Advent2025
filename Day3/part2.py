import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'code.txt')

with open(file_path, 'r') as text:
    banks = [line.strip() for line in text.readlines() if line.strip()]

total = 0

for battery in banks:
    count = 12
    remove = len(battery) - count
    stack = []

    for i in battery:
        while remove> 0 and stack and stack[-1] < i:
            stack.pop()
            remove -= 1
        stack.append(i)

    jolt = ''.join(stack[:count])
    total += int(jolt)

print(total)
