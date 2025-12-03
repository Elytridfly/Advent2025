import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'code.txt')

with open(file_path, 'r') as file:
    content = file.read().strip()

ranges = content.split(',')

parsed_ranges = []
for range_str in ranges:
    parts = range_str.split('-')
    if len(parts) == 2:
        first = int(parts[0])
        last = int(parts[1])
        parsed_ranges.append({'first': first, 'last': last})

print(f"Total ranges loaded: {len(parsed_ranges)}")

while True:
    try:
        index = int(input(f"Enter range index to view (0-{len(parsed_ranges)-1}) or -1 to exit: "))
        
        if index == -1:
            break
        
        if 0 <= index < len(parsed_ranges):
            range_data = parsed_ranges[index]
            print(f"Range {index}: First = {range_data['first']}, Last = {range_data['last']}")
        else:
            print(f"Invalid index. Please enter a number between 0 and {len(parsed_ranges)-1}")
    except ValueError:
        print("Please enter a valid number")
    except KeyboardInterrupt:
        print("\nExiting...")
        break

