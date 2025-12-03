import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'code.txt')

with open(file_path, 'r') as txt:
    values = txt.read().strip().split(',')


def check(i):
     s = (str)(i)
     
     return s in (s + s)[1:-1]

total = 0

for ranges in values:
    head = (int)(ranges.split('-')[0])
    tail = (int)(ranges.split('-')[1])

   
    for i in range(head, tail + 1):
        if check(i):
            total += (int)(i)
        





print(total)