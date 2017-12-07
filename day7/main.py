with open('input') as f:
    data = [line.rstrip() for line in f.readlines()]

disks = {}
for line in data:
    name = line.split('->')[0].split(' ')[0].rstrip()
    weight = int(line.split('->')[0].split(' ')[1].rstrip()[1:-1])
    try:
        others = line.split('->')[1].lstrip().split(', ')
    except IndexError:
        others = []
    disks[name] = (weight, others)

held = []
[held.extend(metadata[1]) for disk_name, metadata in disks.items()]

# Part 1
[print(disk_name) for disk_name, metadata in disks.items() if disk_name not in held]
