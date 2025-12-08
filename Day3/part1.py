import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'code.txt')

with open(file_path, 'r') as text:
    banks = [line.strip() for line in text.readlines() if line.strip()]

total = 0

for battery in banks:
    jolt = 0

    for i in range(len(battery)):
       for j in range(i + 1, len(battery)):
            k = int(battery[i])
            l = int(battery[j])
            m = k*10 + l
            if m > jolt:
                jolt = m


    total += jolt
        
    


print(total)

